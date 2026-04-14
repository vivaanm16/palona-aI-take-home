import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_metrics():
    return {
        "agency_owner": {"open_rate": 0.41, "click_rate": 0.11},
        "freelancer": {"open_rate": 0.55, "click_rate": 0.19},
        "marketing_manager": {"open_rate": 0.48, "click_rate": 0.14}
    }


def analyze(metrics):
    prompt = f"""
You are a marketing analyst.

Analyze this campaign performance data:

{json.dumps(metrics, indent=2)}

Provide:
- 2 insights
- 1 actionable recommendation

Keep it concise and business-focused.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content