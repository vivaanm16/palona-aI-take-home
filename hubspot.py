import requests
import os
from dotenv import load_dotenv

load_dotenv()

HUBSPOT_BASE = "https://api.hubapi.com"
TOKEN = os.getenv("HUBSPOT_API_KEY")


def find_contact_by_email(email):
    url = f"{HUBSPOT_BASE}/crm/v3/objects/contacts/search"

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "filterGroups": [{
            "filters": [{
                "propertyName": "email",
                "operator": "EQ",
                "value": email
            }]
        }]
    }

    res = requests.post(url, headers=headers, json=payload)
    results = res.json().get("results", [])

    return results[0]["id"] if results else None


def upsert_contact(email, persona, newsletter_text):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "properties": {
            "email": email,
            "firstname": "Test",
            "lastname": "User",
            "jobtitle": persona,
            "newsletter_content": newsletter_text[:500]
        }
    }

    contact_id = find_contact_by_email(email)

    if contact_id:
        url = f"{HUBSPOT_BASE}/crm/v3/objects/contacts/{contact_id}"
        res = requests.patch(url, headers=headers, json=payload)
        return res.json()

    else:
        url = f"{HUBSPOT_BASE}/crm/v3/objects/contacts"
        res = requests.post(url, headers=headers, json=payload)
        return res.json()