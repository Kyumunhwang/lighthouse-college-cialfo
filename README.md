# Cialfo.ai — Next-Gen College & Career Readiness (CCR) & Direct Admissions Platform

> **Leaders International School (LIS) — Official 2026 Admissions & Counseling System**  
> Built strictly following `prd.md` specifications and verified high-fidelity interactive UI/UX designs.

---

## 🌟 Platform Highlights

1. **🏛️ Comprehensive 1,510+ Institution Database**
   - Deep integration of **1,504 US Colleges** with IPEDS identifiers, acceptance rates, median SAT/GPA, annual COA/tuition, and financial aid policies (`Need-Blind`, `QuestBridge Partner`, `100% Need Met`).
   - Global elite institutions (UK, Canada, Australia, Singapore, Japan).
   - Fast server-side pagination with state filtering (all 50 US states + DC) and dynamic LIS student admissions fit benchmark (`Reach / Target / Likely`).

2. **🏫 Real School Identity & Data Integrity (Zero Mock Data)**
   - **Real Grade 12 Seniors (17 Students)** extracted from `2026 Fall Semester LIS Student Roster.xlsx` (including passport names, Korean names, student IDs, parent contacts).
   - **Real Faculty & Staff (33 Members)** extracted from `Faculty Roster.xlsx` (Leadership, High School / Middle School teaching staff, extension lines).
   - **Official Leaders International School Emblem** (`emblum.png`) applied universally across letterheads, top-bar navigation, cards, and avatars.

3. **⚡ Direct Apply Benefit Engine & UK Conditional Offer Tracking**
   - Guaranteed fee waivers ($200–$300 saved per submission).
   - Full itemized condition breakdown for UK conditional offers.
   - Embedded real-time **Flywire** multi-currency tuition & deposit payment integration.

4. **✍️ Structured 2-Tier LOR Studio & Multilingual Bridge (PP-01 & PP-08)**
   - **Tier 1 (Common Reflections)**: Auto-synced across all recommenders to eliminate copy-paste friction.
   - **Tier 2 (Course-Specific)**: Individualized academic memory and breakthrough prompts for each teacher.
   - **Multilingual AI Bridge**: Enables non-native English speaking faculty (Korean, Turkish, Spanish, Chinese, French) to input pedagogical notes in their mother tongue, converting them into standard Admissions-Grade Academic English via Gemini AI.

5. **🎓 Counselor Command Center & cDocs Hub**
   - Cohort matrix for Grade 12 applications and Grade 9 quest discovery.
   - Batch cDocs dispatch to Common App & Parchment.
   - Targeted Cialfo Groups multi-channel broadcasting (In-App, Email, Parent SMS).
   - Alumni Scattergram network connecting current seniors with matriculated university mentors.

6. **🤖 Saige AI Copilot**
   - Natural language guidance on diploma equivalencies (e.g., Turkish diploma recognition, foundation years), STEAM dual degrees, and UCAS requirements.

7. **🗄️ Transparent Data Architecture & Ingestion Hub**
   - Complete technical specification of data schemas, verified internet sources, and ready-to-run Python ETL pipelines for every interactive button.

---

## 🛠️ Tech Stack & Architecture

- **Backend / Scripting**: Python 3.11+
- **Frontend / Web UI**: Streamlit with custom CSS design tokens (`Plus Jakarta Sans`, Tailwind palette)
- **Data Storage**: Local JSON store (`data/`) optimized for zero-latency lookups
- **AI Integration**: Google Generative AI (Gemini Pro) SDK
- **Testing**: Native integration & unit test suite (`tests/test_app.py`)

---

## 🚀 Getting Started

### 1. Installation

```bash
git clone https://github.com/Kyumunhwang/lighthouse-college-cialfo.git
cd lighthouse-college-cialfo

# Install dependencies
pip install streamlit openpyxl requests google-generativeai
```

### 2. Run Application

```bash
# Launch Streamlit development server
python -m streamlit run app.py --server.port 3088 --server.headless true
```
Open your browser and navigate to `http://localhost:3088`.

### 3. Run Test Suite

```bash
python tests/test_app.py
```

---

## 📁 Project Structure

```
├── app.py                     # Main application entry point & routing
├── config.py                  # Design system CSS tokens, logo helper & port settings
├── prd.md                     # Product Requirements Document
├── emblum.png                 # Leaders International School official emblem
├── 2026 Fall Semester LIS...  # Grade 12 official senior student roster
├── Faculty Roster.xlsx        # Official academic faculty & staff directory
├── data/                      # Local JSON database
│   ├── student_profile.json   # Active senior profile & gamified quest persona
│   ├── universities.json      # 1,510 global higher education institutions
│   ├── us_colleges_1500.json  # Clean US college dataset with IPEDS & aid policies
│   ├── courses.json           # Curated degree & course catalog
│   ├── applications.json      # Direct Apply submissions & Flywire status
│   ├── lor_requests.json      # 2-Tier LOR state & multilingual AI bridge
│   ├── counselor_data.json    # Counselor metrics, cohorts & alumni network
│   ├── explore_partner.json   # 4-stage funnel & high school visit schedule
│   └── lis_faculty.json       # 33 verified faculty records
├── modules/                   # Modular Python architecture
│   ├── data_manager.py        # Central data access object (DAO)
│   ├── data_pipeline.py       # Data source specifications & ETL guides
│   ├── ai_copilot.py          # Saige AI & Gemini LOR translator
│   ├── ui_utils.py            # Clean HTML renderer
│   └── views/                 # Screen views mirroring design/ HTML
├── design/                    # High-fidelity reference mockups
├── scripts/                   # ETL and data harmonization scripts
└── tests/                     # Integration test suite
```

---

## 📜 License & Compliance

Designed and maintained for Leaders International School (LIS). FERPA, GDPR, and OneRoster 1.2 compliant data architecture.
