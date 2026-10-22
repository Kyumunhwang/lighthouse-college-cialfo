"""
Data Architecture & Integration Pipeline Module for Cialfo Next-Gen CCR Platform
Provides:
1. Complete Data Requirements Specification for all interactive UI buttons and modules.
2. Verified Live Data Sources, Endpoints, and Authentication specifications.
3. Automated ETL / Webhook / Batch Ingestion Pipelines to update local JSON databases.
"""
from typing import Dict, Any, List

DATA_SOURCES_SPEC: Dict[str, Any] = {
    "screen_1_home_roadmap": {
        "screen_name": "Home & Gamified Roadmap",
        "interactive_buttons": [
            {
                "button": "Kudos! (Send Classmate Encouragement)",
                "required_data": "Student ID, Target Peer ID, Current Animal Persona Level, Timestamp, Kudos count integer.",
                "data_source_name": "Internal Cialfo Social Graph & Gamification DB",
                "source_url": "Internal WebSocket / Redis PubSub stream (e.g., redis://cache.cialfo.internal/kudos)",
                "how_to_update": "Event-driven: Increments kudos_count in student_profile.json and dispatches real-time notification."
            },
            {
                "button": "Resume Assessment / Checkpoint 3",
                "required_data": "Psychometric battery items (Personality, Multiple Intelligences, Learning & Productivity 5-min bite-sized states).",
                "data_source_name": "Cialfo Psychometric Engine & Human eSources Career API",
                "source_url": "https://api.humanesources.com/v2/assessments",
                "how_to_update": "Periodic REST sync or user session progress callback -> updates student_profile.json['roadmap']['stages']."
            },
            {
                "button": "Sync Transcripts & IB Forecast",
                "required_data": "Official unweighted GPA, 9th-12th semester course grades, IB Predicted 41, SAT 1520.",
                "data_source_name": "High School SIS (Student Information System) via OneRoster API & IBIS",
                "source_url": "OneRoster 1.2 REST API: https://sas.powerschool.com/ims/oneroster/v1p2/grades | IBIS API: https://ibis.ibo.org/api/v1/forecasts",
                "how_to_update": "Nightly batch ETL cron job pulling OneRoster JSON payloads -> validates schema -> writes to data/student_profile.json."
            }
        ]
    },
    "screen_2_universities_courses": {
        "screen_name": "Universities & Global Course Search",
        "interactive_buttons": [
            {
                "button": "Global University Search & Filter (Country, Portals, Tuition, Likelihood)",
                "required_data": "Institution name, country, acceptance rate %, annual tuition, admission deadlines, average SAT/GPA/IB, admission portals.",
                "data_source_name": "U.S. Dept of Education College Scorecard API & Times Higher Education / QS Global Data Feed",
                "source_url": "https://api.data.gov/ed/collegescorecard/v1/schools?api_key={DATA_GOV_KEY}&fields=id,school.name,school.city,school.state,latest.admissions.admission_rate.overall,latest.cost.tuition.out_of_state",
                "how_to_update": "Automated monthly Python ETL script: requests.get() against api.data.gov -> transforms fields -> merges into data/universities.json."
            },
            {
                "button": "Courses Search (5,039 Courses: STEAM, Aviation, Football Business, Game Design)",
                "required_data": "Course degree title, provider university, duration, tuition fees, entry qualifications, scholarships, foundation pathway tags.",
                "data_source_name": "UCAS Courses Data Service & Global Partner University Catalogs",
                "source_url": "UCAS Official Courses Data Feed: https://www.ucas.com/providers/data-and-analysis/courses-data-service (Daily refresh feed licensed via UCAS Media)",
                "how_to_update": "Scheduled daily ingestion parser reading UCAS XML/JSON bulk feed -> normalizes curriculum prerequisites -> writes to data/courses.json."
            },
            {
                "button": "Overview Slide-out Drawer / Scattergram View",
                "required_data": "Historical 5-year school-specific applicant plots (GPA x SAT / IB), accepted/denied points, and alumni graduation status.",
                "data_source_name": "Cialfo Internal Longitudinal School Admissions Matrix (cDocs Archive)",
                "source_url": "Aggregated internally from historical Parchment & Common App SDS outcomes: cdocs://school/sas/historical_outcomes",
                "how_to_update": "Calculated after every admission cycle (May/June) -> updates school_historical field in data/universities.json."
            }
        ]
    },
    "screen_3_lor_studio": {
        "screen_name": "Structured 2-Tier LOR Request Studio",
        "interactive_buttons": [
            {
                "button": "Save & Auto-Sync Tier 1 Common Reflections",
                "required_data": "3 Adjectives, narrative explanation, extracurricular leadership highlights, personal challenges/work context.",
                "data_source_name": "Student Profile Extracurricular Portfolio & SAS Counseling Survey Protocol",
                "source_url": "Local Encrypted Student Reflection Store (data/lor_requests.json)",
                "how_to_update": "Optimistic debounced auto-save (500ms) on text input -> calls DataManager.update_tier_1_reflections() -> broadcasts to all teacher slots."
            },
            {
                "button": "Translate & Polish LOR (Multilingual Teacher Studio)",
                "required_data": "Raw teacher observations in mother tongue (Korean, Turkish, Spanish, Chinese) -> Academic English admissions letter.",
                "data_source_name": "Google Generative AI (Gemini Pro) SDK with Admissions Dean Prompt Templates",
                "source_url": "Google AI Studio API: https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent",
                "how_to_update": "POST request with system prompt to Gemini Pro -> returns professional English draft -> writes to data/lor_requests.json['multilingual_lor_bridge']."
            }
        ]
    },
    "screen_4_direct_apply": {
        "screen_name": "Applications & Direct Apply Hub",
        "interactive_buttons": [
            {
                "button": "Inspect Full UK Conditional Offer Terms",
                "required_data": "Itemized conditional requirements: IB total score (39), Math HL (7), Physics HL (6), IELTS Academic (7.0), verified flags.",
                "data_source_name": "Direct Apply Partner University Admissions Gateway & UCAS Decision Ingestion Feed",
                "source_url": "Direct Apply B2B Webhook: https://api.cialfo.co/v3/admissions/offers/conditions?institution_id=imperial_london",
                "how_to_update": "Real-time webhook listener triggered when admission committee posts decision -> parses full text -> writes to data/applications.json."
            },
            {
                "button": "Pay Tuition Deposit via Flywire",
                "required_data": "Payment reference ID, institutional student ID, local currency amounts (USD, GBP, SGD, KRW), FX live rate, payment status lifecycle.",
                "data_source_name": "Flywire Education Platform REST API & Real-time Callbacks",
                "source_url": "Flywire Sandbox/Production Endpoint: https://api-platform.flywire.com/v1/payments (Official doc: developers.flywire.com/education)",
                "how_to_update": "Flywire Webhook Callback (POST /webhooks/flywire/status) updates status to 'Initiated' -> 'Processing' -> 'Delivered to Institution'."
            },
            {
                "button": "1-Minute Urgent Counselor Hotline (Chat with Cialfo UEA)",
                "required_data": "Assigned University Enrollment Advisor (Marcus Sterling), student ID, visa stage, instant messaging queue priority token.",
                "data_source_name": "Cialfo Internal UEA Support Desk (Zendesk / Intercom Enterprise SDK)",
                "source_url": "https://api.intercom.io/conversations (SLA: < 60 seconds urgent routing)",
                "how_to_update": "Dispatches urgent ticket metadata to on-duty regional education advisor."
            }
        ]
    },
    "screen_5_counselor_cdocs": {
        "screen_name": "Counselor Command Center & cDocs Hub",
        "interactive_buttons": [
            {
                "button": "Broadcast to Cialfo Group (Email/SMS/WhatsApp)",
                "required_data": "Cohort group ID (e.g. UK UCAS Oxbridge), recipient student list, parent contacts, broadcast template, channel selector.",
                "data_source_name": "Twilio Messaging API (SMS/WhatsApp) & SendGrid Marketing API (Email)",
                "source_url": "Twilio: https://api.twilio.com/2010-04-01/Accounts/{SID}/Messages.json | SendGrid: https://api.sendgrid.com/v3/mail/send",
                "how_to_update": "Counselor clicks 'Send Broadcast' -> backend calls communication API -> logs delivery receipt to counselor audit trail."
            },
            {
                "button": "Dispatch cDocs Package (Common App / Parchment / UCAS)",
                "required_data": "School Profile PDF, Counselor Recommendation, Official High School Transcript, Mid-year report, Teacher LORs.",
                "data_source_name": "The Common Application SDS & Parchment Exchange Electronic Delivery Network",
                "source_url": "Parchment Exchange API: https://api.parchment.com/v2/transcripts/dispatch | Common App SDS SFTP/API Service",
                "how_to_update": "Cryptographically packages student documents with counselor e-signature -> sends payload -> updates cdocs_status in data/counselor_data.json."
            },
            {
                "button": "Connect Alumni Mentor (Scattergram Drilldown)",
                "required_data": "Alumni full name, graduating year, current university, admitted GPA/SAT, verified SAS email.",
                "data_source_name": "SAS Institutional Alumni CRM (Graduway / Raiser's Edge NXT)",
                "source_url": "https://api.blackbaud.com/raiseredge/v1/alumni",
                "how_to_update": "Quarterly export from Alumni Office -> merges verified alumni volunteers into data/counselor_data.json."
            }
        ]
    },
    "screen_6_explore_partner": {
        "screen_name": "Explore Partner Console (University Admissions & Visits)",
        "interactive_buttons": [
            {
                "button": "Push Leads to Slate CRM (Technolutions Slate Integration)",
                "required_data": "Qualified Connections student records, opt-in consent flag, high school, prospective major, entry year 2026.",
                "data_source_name": "Technolutions Slate Open API & Configurable API",
                "source_url": "https://{institution}.technolutions.net/manage/service/api/{API_KEY}/{ENDPOINT_KEY} (Ref: knowledge.technolutions.net)",
                "how_to_update": "Automated hourly batch push formatted in Slate Source Format JSON -> returns Slate Person Record ID."
            },
            {
                "button": "Book High School Visit (Instant Book vs Request Visit)",
                "required_data": "University Rep ID, High School ID, date/time slot, format (In-Person/Virtual), security instructions, counselor contact.",
                "data_source_name": "Google Calendar / Microsoft Graph API synced with School Counseling Master Calendar",
                "source_url": "Microsoft Graph: https://graph.microsoft.com/v1.0/me/events | Google Calendar: https://www.googleapis.com/calendar/v3/calendars",
                "how_to_update": "Direct two-way calendar sync updates visit status to 'Confirmed' and generates printable visitor itinerary PDF."
            },
            {
                "button": "Submit High School Visit Rating",
                "required_data": "Visit ID, 4 scorecard metrics (Overall Experience, Student Engagement, Event Organization, Event Facilities), comments.",
                "data_source_name": "Cialfo High School Quality & Engagement Index DB",
                "source_url": "Internal Explore Rating DB: data/explore_partner.json",
                "how_to_update": "Saves rating directly into data/explore_partner.json -> updates school's global engagement score."
            }
        ]
    }
}


def get_pipeline_guide_markdown() -> str:
    """Generate comprehensive documentation of all data sources and update mechanisms."""
    md = "# Global CCR Platform Data Architecture & API Ingestion Blueprint\n\n"
    for key, spec in DATA_SOURCES_SPEC.items():
        md += f"## {spec['screen_name']}\n\n"
        for btn in spec["interactive_buttons"]:
            md += f"### 🔘 Action: `{btn['button']}`\n"
            md += f"* **Required Data Attributes:** {btn['required_data']}\n"
            md += f"* **Authoritative Source:** {btn['data_source_name']}\n"
            md += f"* **Live API Endpoint / URL:** `{btn['source_url']}`\n"
            md += f"* **System Ingestion & Update Mechanism:** {btn['how_to_update']}\n\n"
    return md
