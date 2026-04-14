# NovaMind AI Marketing Pipeline

## Overview

This project is an automated AI-driven marketing pipeline that generates blog content.

---

## Architecture Overview and Flow

User Input (Topic)  
→ AI Content Generation (Groq LLM)  
→ Blog + Persona-Based Newsletters  
→ CRM Integration (HubSpot Contacts API)  
→ Create/Update Contacts + Persona Tagging  
→ Store Newsletter Preview in Contact Properties  
→ Simulated Newsletter Distribution  
→ Campaign Logging (local JSON file)  
→ Metrics Gegit remoteneration (simulated)  
→ AI-Based Performance Analysis (Groq)  
→ Streamlit Dashboard for Visualization

---

## Tools, APIs, and Models Used

### AI Model
- Groq API
- Model: llama-3.1-8b-instant
- Used for blog generation, newsletter personalization, and performance analysis

### CRM
- HubSpot CRM API
- Endpoints:
  - POST /crm/v3/objects/contacts
  - PATCH /crm/v3/objects/contacts/{id}
  - POST /crm/v3/objects/contacts/search
- Used for:
  - Contact creation and updates
  - Persona tagging (jobtitle field)
  - Storing newsletter content (newsletter_content property)

### Frontend
- Streamlit
- Used for triggering the pipeline and displaying outputs

### Other Libraries
- requests
- python-dotenv
- json
- datetime

---

## Assumptions

- HubSpot API token is valid and stored in environment variables
- Contacts are identified uniquely by email and updated via upsert logic
- Newsletter sending is simulated and not delivered via email service
- A custom HubSpot property (newsletter_content) exists for storing newsletter text
- Engagement metrics are simulated rather than collected from real users
- All execution is local (no deployment environment required)

---

## Instructions to Run Locally

### 1. Clone repository
```bash
git clone <repo-url>
cd NovaMind

pip install -r requirements.txt
streamlit run dashboard.py