import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_content(topic):
    prompt = f"""
    Topic: {topic}

    Generate:
    - Blog title
    - Outline (3-5 bullets)
    - Blog (400-600 words)
    - 3 newsletters for:
      * Creative Agency Owner
      * Freelancer
      * Marketing Manager

    Return strict JSON:
    {{
      "blog": {{
        "title": "",
        "outline": [],
        "content": ""
      }},
      "newsletters": {{
        "agency_owner": "",
        "freelancer": "",
        "marketing_manager": ""
      }}
    }}
    """

    messages = [{"role": "user", "content": prompt}]

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.7,
        response_format={"type": "json_object"}
    )

    return json.loads(response.choices[0].message.content)
