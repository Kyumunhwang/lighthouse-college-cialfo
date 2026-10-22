"""
Convert and populate Cialfo databases using real student data from 
2026 Fall Semester LIS Student Roster.xlsx
"""
import openpyxl
import json
from pathlib import Path

excel_path = Path("2026 Fall Semester LIS Student Roster.xlsx")
wb = openpyxl.load_workbook(excel_path, data_only=True)
sheet = wb["International"]

cur_section = ""
cur_teacher = ""

roster = []

for r in range(4, sheet.max_row + 1):
    vals = [cell.value for cell in sheet[r]]
    if not any(vals):
        continue
    
    sec_cell = vals[1]
    teacher_cell = vals[2]
    if sec_cell is not None and str(sec_cell).strip():
        cur_section = str(sec_cell).strip().replace('\n', ' ')
    if teacher_cell is not None and str(teacher_cell).strip():
        cur_teacher = str(teacher_cell).strip().replace('\n', ' ')
        
    k_name = vals[3]
    passport_name = vals[4]
    eng_name = vals[5]
    stu_id = vals[6]
    zip_code = vals[7]
    address = vals[8]
    gender = vals[9]
    grade_val = vals[10]
    dob = vals[11]
    father = vals[12] if len(vals) > 12 and vals[12] else ""
    mother = vals[13] if len(vals) > 13 and vals[13] else ""
    cell_phone = vals[15] if len(vals) > 15 and vals[15] else ""
    remarks = vals[19] if len(vals) > 19 and vals[19] else ""
    
    if k_name and stu_id:
        student = {
            "row": r,
            "section": cur_section,
            "homeroom_teacher": cur_teacher,
            "korean_name": str(k_name).strip(),
            "passport_name": str(passport_name).strip() if passport_name else str(k_name).strip(),
            "english_name": str(eng_name).strip() if eng_name else str(passport_name).strip(),
            "student_id": str(stu_id).strip(),
            "grade": grade_val,
            "dob": str(dob).strip() if dob else "",
            "gender": str(gender).strip() if gender else "",
            "address": str(address).strip() if address else "",
            "father": str(father).strip(),
            "mother": str(mother).strip(),
            "cell": str(cell_phone).strip(),
            "remarks": str(remarks).strip()
        }
        roster.append(student)

h12_students = [s for s in roster if "H12" in s["section"]]
h11_students = [s for s in roster if "H11" in s["section"]]
h10_students = [s for s in roster if "H10" in s["section"]]
h9_students = [s for s in roster if "H9" in s["section"]]

print(f"Loaded {len(roster)} total students. High school breakdown: H12={len(h12_students)}, H11={len(h11_students)}, H10={len(h10_students)}, H9={len(h9_students)}")

# 1. Build real students database for LIS
# Default active student: Sumin Cho (조수민, ID: 2019F0502, English Name: Ella, Homeroom: Peter Yoo)
primary_student = h12_students[1] # Sumin Cho

student_profile_data = {
    "active_student_id": primary_student["student_id"],
    "student": {
        "student_id": primary_student["student_id"],
        "name": f"{primary_student['passport_name']} ({primary_student['korean_name']})",
        "english_name": primary_student["english_name"] or "Ella",
        "korean_name": primary_student["korean_name"],
        "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&auto=format&fit=crop&q=80",
        "grade": "12th Grader (H12)",
        "cohort": "Class of 2026",
        "school": "Leaders International School (LIS)",
        "homeroom_teacher": primary_student["homeroom_teacher"] or "Peter Yoo",
        "counselor": "Peter Yoo (Director of College Counseling)",
        "curriculum": "AP & International College Prep",
        "gpa_unweighted": 3.94,
        "sat_score": 1530,
        "ib_predicted": 40,
        "dob": primary_student["dob"],
        "gender": primary_student["gender"],
        "address": primary_student["address"],
        "guardians": {
            "father": primary_student["father"] or "조기웅",
            "mother": primary_student["mother"] or "정미경",
            "contact": primary_student["cell"]
        },
        "active_applications_count": 6,
        "countries_targeted": ["United States", "United Kingdom", "Australia", "Canada"],
        "direct_apply_partner_status": "Active"
    },
    "all_h12_seniors": [
        {
            "student_id": s["student_id"],
            "passport_name": s["passport_name"],
            "korean_name": s["korean_name"],
            "english_name": s["english_name"],
            "display_name": f"{s['passport_name']} ({s['korean_name']}) - {s['english_name'] or 'Senior'}",
            "gender": s["gender"],
            "dob": s["dob"],
            "homeroom_teacher": s["homeroom_teacher"],
            "father": s["father"],
            "mother": s["mother"],
            "cell": s["cell"],
            "address": s["address"]
        }
        for s in h12_students
    ],
    "roadmap": {
        "current_stage": 3,
        "stage_title": "Stage 3 of 4: In High Gear (70% Overall Readiness)",
        "cycle": "FALL 2026 CYCLE",
        "next_critical_date": "Nov 1 (US Early Decision & UK Early Deadlines)",
        "stages": [
            {
                "id": 1,
                "name": "Profile & Foundation",
                "description": "LIS transcript, GPA 3.94, demographics, parent info locked.",
                "progress": 100,
                "status": "Done"
            },
            {
                "id": 2,
                "name": "Discovery & Quest",
                "description": "Major matches (Computing & Business), career assessments completed.",
                "progress": 100,
                "status": "Done"
            },
            {
                "id": 3,
                "name": "Build Lists & Apply",
                "description": "Common App linked, LOR requested from Peter Yoo, Direct Apply in progress.",
                "progress": 70,
                "status": "In Progress"
            },
            {
                "id": 4,
                "name": "Offer, Flywire & Enroll",
                "description": "Conditional offers, Flywire tuition deposit, and student visa processing.",
                "progress": 15,
                "status": "Upcoming"
            }
        ]
    },
    "quest_persona": {
        "level": 4,
        "name": "Applying Alpaca",
        "badge": "🦙 Space Suit Alpaca",
        "tagline": "LIS Class of 2026 Senior executing multi-country early applications.",
        "focus_area": "Finalizing LOR Tier 2 responses for Peter Yoo & Direct Apply submissions",
        "what_to_embrace": "Locking Section B reflections and verifying UK / US Early Decision deadlines early.",
        "what_to_avoid": "Leaving transcript dispatch and Flywire deposit transactions to deadline night.",
        "kudos_count": 56,
        "progression_ladder": [
            {"level": 1, "animal": "Curious Capybara", "focus": "Self-Discovery & Course Selection"},
            {"level": 2, "animal": "Exploring Elephant", "focus": "University Longlist Building"},
            {"level": 3, "animal": "List-Building Leopard", "focus": "Scattergram & Fit Calibration"},
            {"level": 4, "animal": "Applying Alpaca", "focus": "Global Applications & Direct Apply"}
        ]
    },
    "classmate_kudos": [
        {"student": f"{h12_students[0]['passport_name']} ({h12_students[0]['korean_name']})", "persona": "Applying Alpaca", "action": "Submitted Direct Apply to Imperial College", "time": "15m ago"},
        {"student": f"{h12_students[3]['passport_name']} ({h12_students[3]['korean_name']})", "persona": "Applying Alpaca", "action": "Locked 6 Shortlisted US universities", "time": "38m ago"},
        {"student": f"{h12_students[7]['passport_name']} ({h12_students[7]['korean_name']})", "persona": "List-Building Leopard", "action": "Completed Common App Personal Essay Draft v3", "time": "1h ago"},
        {"student": f"{h12_students[8]['passport_name']} ({h12_students[8]['korean_name']})", "persona": "Applying Alpaca", "action": "Requested LOR from Peter Yoo", "time": "2h ago"}
    ],
    "urgent_tasks": [
        {"id": "task-lis-1", "title": "Submit Final Draft for Common App Personal Statement", "due": "Oct 25", "priority": "Urgent", "status": "In Progress", "type": "Essay Task"},
        {"id": "task-lis-2", "title": "Confirm Section B Recommender Form for Peter Yoo", "due": "Oct 28", "priority": "High", "status": "Action Required", "type": "LOR Task"},
        {"id": "task-lis-3", "title": "Upload Valid Passport Copy to Personal Hubs Drive", "due": "Nov 02", "priority": "Medium", "status": "Not Started", "type": "Document Task"}
    ],
    "counselor_notes": {
        "date": "Oct 22, 2026",
        "counselor": "Peter Yoo (Director of Counseling / H12 Homeroom)",
        "summary": f"Met with {primary_student['passport_name']} ({primary_student['korean_name']}). GPA of 3.94 and SAT 1530 make her an excellent candidate for NYU Stern, Imperial College Computing, and University of Sydney Direct Apply. Verified guardian contacts: {primary_student['father']} & {primary_student['mother']}.",
        "action_items": [
            "Complete Tier 2 course reflection for AP/IB Literature and Physics",
            "Activate Cialfo Direct Apply fee waiver for Australia and UK submissions"
        ]
    }
}

with open("data/student_profile.json", "w", encoding="utf-8") as f:
    json.dump(student_profile_data, f, indent=2, ensure_ascii=False)
print("Updated data/student_profile.json with real LIS student data!")

# 2. Build counselor_data.json with ALL real students from H12 and H9
students_table_records = []
target_countries_sample = [
    ["US", "UK"], ["US", "AU"], ["UK", "CA"], ["US", "KR"],
    ["UK", "AU", "US"], ["US", "SG"], ["US", "CA"]
]
cdocs_status_sample = ["Ready to Send", "Dispatched", "Missing Teacher Rec", "Drafting Essays", "Approved to Send"]
likelihood_sample = ["Target", "Reach", "Likely", "Target", "Reach"]

for idx, s in enumerate(h12_students):
    students_table_records.append({
        "id": s["student_id"],
        "name": f"{s['korean_name']} ({s['passport_name']})",
        "english_name": s["english_name"] or "Senior",
        "grade": "12",
        "section": "H12",
        "homeroom_teacher": s["homeroom_teacher"] or "Peter Yoo",
        "persona": "Applying Alpaca",
        "curriculum": "AP & Honors (GPA 3.85-3.98)",
        "target_countries": target_countries_sample[idx % len(target_countries_sample)],
        "apps_count": 5 + (idx % 4),
        "cdocs_status": cdocs_status_sample[idx % len(cdocs_status_sample)],
        "first_deadline": "Nov 1 (Early Decision)" if idx % 2 == 0 else "Nov 15",
        "counselor_likelihood_override": likelihood_sample[idx % len(likelihood_sample)],
        "father": s["father"],
        "mother": s["mother"],
        "cell": s["cell"]
    })

# Add H9 freshmen records for the 9th grade view
for idx, s in enumerate(h9_students):
    students_table_records.append({
        "id": s["student_id"],
        "name": f"{s['korean_name']} ({s['passport_name']})",
        "english_name": s["english_name"] or "Freshman",
        "grade": "9",
        "section": "H9",
        "homeroom_teacher": s["homeroom_teacher"] or "Michelle Lee",
        "persona": "Exploring Elephant" if idx % 2 == 0 else "Curious Capybara",
        "curriculum": "High School Pre-College Prep",
        "target_countries": ["Undecided"],
        "apps_count": 0,
        "cdocs_status": "Career Assessment Complete" if idx % 2 == 0 else "In Progress",
        "first_deadline": "N/A",
        "counselor_likelihood_override": "N/A",
        "father": s["father"],
        "mother": s["mother"],
        "cell": s["cell"]
    })

counselor_data_payload = {
    "counselor": {
        "name": "Peter Yoo",
        "role": "Director of College & Career Counseling / H12 Homeroom",
        "school": "Leaders International School (LIS)",
        "assigned_students": len(h12_students),
        "total_cohort_12th": len(h12_students),
        "total_cohort_11th": len(h11_students),
        "total_cohort_10th": len(h10_students),
        "total_cohort_9th": len(h9_students),
        "total_high_school": len(h12_students) + len(h11_students) + len(h10_students) + len(h9_students)
    },
    "cohort_metrics": {
        "avg_countries_per_student": 3.2,
        "total_applications_active": sum(s["apps_count"] for s in students_table_records if s["grade"] == "12"),
        "direct_apply_adoption": "76%",
        "total_fee_waivers_saved_usd": 24800,
        "cdocs_dispatched_rate": "82%"
    },
    "cialfo_groups": [
        {
            "id": "grp-lis-1",
            "name": "LIS US Early Decision & Action Cohort",
            "student_count": 12,
            "deadline": "Nov 1",
            "status": "Transcripts & School Profile Dispatched via Parchment",
            "tags": ["Common App", "ED/EA", "Parchment"]
        },
        {
            "id": "grp-lis-2",
            "name": "LIS UK UCAS & Direct Apply Aspirants",
            "student_count": 8,
            "deadline": "Oct 15 / Jan 29",
            "status": "Conditional Offer Full Term Tracking & Personal Statements",
            "tags": ["Direct Apply", "UCAS", "UK"]
        },
        {
            "id": "grp-lis-3",
            "name": "LIS Direct Apply Global Fast-Track (AU & CA)",
            "student_count": 10,
            "deadline": "Dec 15",
            "status": "Fee Waivers Validated / Flywire Payment Integration",
            "tags": ["Direct Apply", "Flywire", "Australia"]
        },
        {
            "id": "grp-lis-4",
            "name": "LIS 9th & 10th Grade Career & Quest Cohort",
            "student_count": len(h9_students) + len(h10_students),
            "deadline": "End of Fall Term",
            "status": "3-Tier Psychometric & Personality Assessment",
            "tags": ["Quest", "Career", "Freshmen"]
        }
    ],
    "students_table": students_table_records,
    "alumni_scattergram_network": [
        {
            "university": "Imperial College London",
            "alumni_name": "Min-woo Park (LIS '23)",
            "program": "BSc Computing",
            "admit_stats": "GPA 3.96, SAT 1540",
            "mentorship_available": True,
            "email": "minwoo.park.alumni@lis.ac.kr"
        },
        {
            "university": "New York University (Stern)",
            "alumni_name": "Ji-won Kang (LIS '24)",
            "program": "BS Business & Finance",
            "admit_stats": "GPA 3.95, SAT 1520",
            "mentorship_available": True,
            "email": "jiwon.kang.alumni@lis.ac.kr"
        },
        {
            "university": "University of Sydney",
            "alumni_name": "Hyun-woo Lee (LIS '22)",
            "program": "Bachelor of Advanced Computing",
            "admit_stats": "GPA 3.82, SAT 1460",
            "mentorship_available": True,
            "email": "hyunwoo.lee.alumni@lis.ac.kr"
        }
    ]
}

with open("data/counselor_data.json", "w", encoding="utf-8") as f:
    json.dump(counselor_data_payload, f, indent=2, ensure_ascii=False)
print("Updated data/counselor_data.json with real LIS students and counselor Peter Yoo!")

# 3. Update lor_requests.json with real teachers
lor_data_payload = {
    "cap_policy": {
        "max_allowed": 2,
        "requested_count": 1,
        "policy_note": "Leaders International School (LIS) limits teacher recommendations to 2 core high school faculty members (Math, Science, English, Social Sciences).",
        "status": "1 / 2 Recommenders Requested"
    },
    "tier_1_common_reflections": {
        "three_adjectives": "Resilient, Analytical, Compassionate",
        "adjectives_explanation": f"As an LIS senior, I combine rigorous STEM problem solving with active community contribution in Ilsan and Paju.",
        "extracurricular_highlights": "LIS Student Council Secretary, Leader of Coding Club, Volunteer tutoring middle school students.",
        "background_challenges": f"Balancing rigorous AP coursework with supporting my family in {primary_student['address'][:15] if primary_student['address'] else 'Ilsan'}.",
        "auto_sync_enabled": True,
        "last_saved": "2026-10-22 22:30 KST"
    },
    "recommenders": [
        {
            "id": "rec-lis-1",
            "teacher_name": "Peter Yoo",
            "subject": "AP Literature & College Seminar",
            "department": "Humanities & Counseling",
            "status": "In Progress (Teacher Reviewing)",
            "requested_date": "2026-09-30",
            "deadline": "2026-10-28",
            "tier_2_course_reflections": {
                "memorable_project": "Comparative textual analysis on global ethics and technological displacement in 21st century society.",
                "intellectual_growth": "Formulating nuanced philosophical arguments and articulating complex literary perspectives in English seminar debates.",
                "link_to_target_major": "Essential for interdisciplinary technology leadership, business ethics, and data communication."
            },
            "teacher_submission": {
                "has_submitted": False,
                "input_language": "English",
                "draft_status": "Draft v2 in progress"
            }
        },
        {
            "id": "rec-lis-2",
            "teacher_name": "David Nah",
            "subject": "AP Physics & Advanced Mathematics",
            "department": "Science & Mathematics",
            "status": "Ready for Request",
            "requested_date": "2026-10-22",
            "deadline": "2026-11-05",
            "tier_2_course_reflections": {
                "memorable_project": "Design and telemetry analysis of an autonomous sensor-driven rover for robotics laboratory experiments.",
                "intellectual_growth": "Mastering differential equations and computational modeling to predict real-world physical oscillations.",
                "link_to_target_major": "Directly foundational for undergraduate Computer Science, Engineering, and Quantitative Economics."
            },
            "teacher_submission": {
                "has_submitted": False,
                "input_language": "Korean",
                "draft_status": "Ready for submission"
            }
        }
    ],
    "multilingual_lor_bridge": {
        "enabled": True,
        "description": "For LIS faculty writing recommendations in Korean. Gemini AI transforms raw Korean notes into academic admissions English for Peter Yoo's review.",
        "sample_input_language": "Korean",
        "sample_raw_teacher_notes": f"{primary_student['korean_name']} 학생은 LIS 재학 기간 동안 학업에 매우 성실하고 탐구심이 강했습니다. 특히 물리와 수학 과목에서 높은 분석력을 발휘하며 친구들을 배려하고 이끄는 모범적인 리더십을 보였습니다.",
        "ai_converted_english_draft": f"\"{primary_student['passport_name']} ({primary_student['korean_name']}) has consistently demonstrated exceptional intellectual curiosity and exemplary scholarly discipline at Leaders International School. In advanced mathematics and analytical sciences, she showcases mature problem-solving abilities paired with profound collaborative empathy. She represents the highest standard of academic excellence and integrity.\"",
        "counselor_approval_status": "Approved to cDocs Queue"
    }
}

with open("data/lor_requests.json", "w", encoding="utf-8") as f:
    json.dump(lor_data_payload, f, indent=2, ensure_ascii=False)
print("Updated data/lor_requests.json with real LIS teachers and student reflections!")
