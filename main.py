import json
import os
from datetime import datetime

from generate import generate_content
from analysis import generate_metrics, analyze
from hubspot import upsert_contact

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def send_newsletter(persona, newsletter_text):

    print(f"Sending newsletter to {persona}...")

    return {
        "persona": persona,
        "status": "sent",
        "content_preview": newsletter_text[:100]
    }


def run_pipeline(topic):
    print("\nStarting pipeline...\n")

    os.makedirs("data", exist_ok=True)


    # AI CONTENT GENERATION
    content = generate_content(topic)

    with open("data/content.json", "w") as f:
        json.dump(content, f, indent=2)

    print("Content generated")


    # CRM + NEWSLETTER PIPELINE
    personas = {
        "agency_owner": "agency@test.com",
        "freelancer": "freelancer@test.com",
        "marketing_manager": "marketing@test.com"
    }

    campaign_log = []

    for persona, email in personas.items():


        newsletter = content["newsletters"][persona]
        upsert_contact(email, persona, newsletter)


        newsletter = content["newsletters"][persona]
        send_newsletter(persona, newsletter)


        campaign_log.append({
            "blog_title": content["blog"]["title"],
            "persona": persona,
            "send_date": datetime.utcnow().isoformat()
        })

    with open("data/campaigns.json", "w") as f:
        json.dump(campaign_log, f, indent=2)

    print("CRM + campaigns logged")


    # METRICS

    metrics = generate_metrics()

    with open("data/metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    print("Metrics generated")


    # AI ANALYSIS

    summary = analyze(metrics)

    with open("data/analysis.txt", "w") as f:
        f.write(summary)

    print("\nINSIGHTS:\n")
    print(summary)

    print("\nPipeline complete!")


if __name__ == "__main__":
    topic = input("Enter blog topic: ")
    run_pipeline(topic)