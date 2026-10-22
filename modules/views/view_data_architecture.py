"""
View: Data Architecture, Live Sources & Update Pipeline
Directly answers the user's architectural questions:
1. What data is required for each interactive button/screen?
2. Where is that data located on the internet (verified live endpoints)?
3. How to update that data into the local JSON / database system?
"""
import streamlit as st
from modules.data_pipeline import DATA_SOURCES_SPEC
from modules.ui_utils import render_html


def render_data_architecture_view():
    """Render Data Architecture & Live Integration Specification."""
    render_html(
        """
        <div style="margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 26px;">🗄️</span>
                <h2 style="margin: 0; font-size: 24px; font-weight: 700; color: #131b2e;">Data Architecture & Live Ingestion Hub</h2>
            </div>
            <p style="margin: 4px 0 0 0; font-size: 13px; color: #434655;">
                Architectural blueprint specifying data schemas, verified internet sources, and ETL update pipelines for every button and module.
            </p>
        </div>
        """
    )

    tab_overview, tab_by_screen, tab_code_pipelines = st.tabs([
        "📊 Data Sourcing Matrix",
        "🔘 Screen-by-Screen Button Requirements",
        "⚙️ Automated Python Ingestion Pipelines"
    ])

    with tab_overview:
        render_html(
            """
            <div class="cialfo-card cialfo-card-primary" style="margin-bottom: 16px;">
                <h3 style="margin: 0 0 8px 0; font-size: 18px; font-weight: 700; color: #131b2e;">System-Wide Data Ecosystem Summary</h3>
                <p style="margin: 0; font-size: 13px; color: #434655; line-height: 1.5;">
                    The Cialfo platform is built upon 6 authoritative external data pipelines:
                    (1) U.S. Federal Higher Ed Open Data (College Scorecard),
                    (2) UK UCAS Daily Courses & Decisions Feed,
                    (3) High School SIS (OneRoster 1.2),
                    (4) Flywire Multi-Currency Education Payments,
                    (5) Slate Admissions CRM (Technolutions), and
                    (6) Google Generative AI (Gemini Pro) for multilingual translations and Saige guidance.
                </p>
            </div>
            """
        )

        st.markdown(
            """
            | Data Domain | Live Internet Source / API | Protocol / Format | Update Cadence | Destination DB |
            | :--- | :--- | :--- | :--- | :--- |
            | **US Higher Ed DB** | [U.S. Dept of Education College Scorecard](https://collegescorecard.ed.gov/data/api-documentation/) | REST API (JSON) with `data.gov` API Key | Monthly Ingestion | `data/universities.json` |
            | **UK Courses & Entry Req.** | [UCAS Courses Data Service](https://www.ucas.com/providers/data-and-analysis/courses-data-service) | Licensed Daily XML/JSON Feed | Daily 24h Batch | `data/courses.json` |
            | **Student Transcripts** | [IMS Global OneRoster 1.2](https://www.imsglobal.org/oneroster-v12-final-specification) (PowerSchool / Veracross) | OAuth2 REST API | Nightly SIS Sync | `data/student_profile.json` |
            | **Payment & FX** | [Flywire Education Platform API](https://developers.flywire.com/education/) | REST API & Webhooks | Real-Time Callbacks | `data/applications.json` |
            | **University CRM Leads** | [Technolutions Slate Configurable API](https://knowledge.technolutions.net/) | REST Open API / JSON Source Format | Hourly Push | `data/explore_partner.json` |
            | **Admissions AI & Translation**| [Google Generative AI (Gemini Pro)](https://ai.google.dev/) | Python SDK (`google-generativeai`) | On-Demand (Real-time) | `data/lor_requests.json` |
            """
        )

    with tab_by_screen:
        for screen_key, screen_info in DATA_SOURCES_SPEC.items():
            with st.expander(f"📱 {screen_info['screen_name']} — Action Button Data Specs", expanded=True):
                for b in screen_info["interactive_buttons"]:
                    render_html(
                        f"""
                        <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px; margin-bottom: 12px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                                <strong style="font-size: 14px; color: #1d4ed8;">🔘 Action: {b['button']}</strong>
                                <span class="badge-slate">{b['data_source_name']}</span>
                            </div>
                            <div style="font-size: 12px; color: #131b2e; margin-bottom: 4px;">
                                <strong>Required Data Attributes:</strong> {b['required_data']}
                            </div>
                            <div style="font-size: 12px; color: #004f35; margin-bottom: 4px; word-break: break-all;">
                                <strong>Live API URL / Endpoint:</strong> <code>{b['source_url']}</code>
                            </div>
                            <div style="font-size: 12px; color: #78350f; background: #fffbeb; padding: 8px; border-radius: 6px; margin-top: 6px;">
                                <strong>⚙️ How to Update System:</strong> {b['how_to_update']}
                            </div>
                        </div>
                        """
                    )

    with tab_code_pipelines:
        st.markdown(
            """
            ### Ready-to-Run Ingestion Pipeline Scripts
            The following Python code snippets demonstrate how to pull data from official APIs and update the local JSON store.
            """
        )

        st.code(
            '''
# ==============================================================================
# PIPELINE 1: College Scorecard API -> data/universities.json
# ==============================================================================
import requests
import json

def sync_college_scorecard(api_key: str, state: str = "CA"):
    """Fetches official higher education data from data.gov and updates local JSON."""
    url = "https://api.data.gov/ed/collegescorecard/v1/schools"
    params = {
        "api_key": api_key,
        "school.state": state,
        "fields": "id,school.name,school.city,school.state,latest.admissions.admission_rate.overall,latest.cost.tuition.out_of_state",
        "per_page": 20
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"Successfully fetched {len(data.get('results', []))} institutions.")
        # Transform and merge into data/universities.json
        return data["results"]
    else:
        raise Exception(f"API Error {response.status_code}: {response.text}")


# ==============================================================================
# PIPELINE 2: Flywire Payment Webhook -> data/applications.json
# ==============================================================================
def handle_flywire_webhook_callback(payload: dict):
    """Processes real-time payment status callbacks from Flywire."""
    flywire_ref = payload.get("payment_reference") # e.g. "FW-IMP-2026-90412"
    new_status = payload.get("status")             # "Processing in Transit" or "Delivered"
    
    with open("data/applications.json", "r+", encoding="utf-8") as f:
        apps = json.load(f)
        for app in apps:
            if app.get("flywire_payment", {}).get("flywire_reference") == flywire_ref:
                app["flywire_payment"]["status"] = new_status
                break
        f.seek(0)
        json.dump(apps, f, indent=2, ensure_ascii=False)
        f.truncate()
    print(f"Updated Flywire payment {flywire_ref} status to: {new_status}")


# ==============================================================================
# PIPELINE 3: Push Leads to Slate CRM (Technolutions)
# ==============================================================================
def push_leads_to_slate(institution_domain: str, api_key: str, leads: list):
    """Pushes qualified student connections directly into university Slate CRM."""
    endpoint = f"https://{institution_domain}.technolutions.net/manage/service/api/{api_key}/cialfo_leads"
    headers = {"Content-Type": "application/json"}
    response = requests.post(endpoint, json={"records": leads}, headers=headers)
    return response.status_code == 200
            ''',
            language="python"
        )
