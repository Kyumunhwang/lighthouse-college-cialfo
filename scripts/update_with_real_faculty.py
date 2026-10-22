"""
Update Cialfo databases with authentic faculty roster from Faculty Roster.xlsx
"""
import json
from pathlib import Path

# Load parsed faculty
with open("data/lis_faculty.json", "r", encoding="utf-8") as f:
    faculty_list = json.load(f)

# 1. Update counselor_data.json
with open("data/counselor_data.json", "r", encoding="utf-8") as f:
    counselor_data = json.load(f)

counselor_data["counselor"] = {
    "name": "David Nah (나경식)",
    "english_name": "David Nah",
    "korean_name": "나경식",
    "role": "College Counselor & H11 Homeroom",
    "school": "Leaders International School (LIS)",
    "principal": "Paul Kim (김바울 - Headmaster / Principal)",
    "vice_principal_secondary": "Kyu Mun Hwang (황규문 - Vice Principal / Computer Science)",
    "h12_homeroom": "Peter Yoo (유찬호 - Chaplain / H12 Homeroom)",
    "registrar": "Jae Lee (이재원 - Registrar / Secondary Student Services Director)",
    "extension": "213",
    "assigned_students": 17,
    "total_cohort_12th": 17,
    "total_cohort_11th": 8,
    "total_cohort_10th": 18,
    "total_cohort_9th": 15,
    "total_high_school": 58
}

counselor_data["faculty_directory"] = faculty_list

with open("data/counselor_data.json", "w", encoding="utf-8") as f:
    json.dump(counselor_data, f, indent=2, ensure_ascii=False)
print("Updated counselor_data.json with real faculty directory and counselor David Nah!")

# 2. Update student_profile.json
with open("data/student_profile.json", "r", encoding="utf-8") as f:
    student_profile = json.load(f)

student_profile["student"]["counselor"] = "David Nah (나경식 - College Counselor, Ext: 213)"
student_profile["student"]["homeroom_teacher"] = "Peter Yoo (유찬호 - H12 Homeroom / Chaplain)"
student_profile["counselor_notes"] = {
    "date": "Oct 22, 2026",
    "counselor": "David Nah (College Counselor) & Peter Yoo (H12 Homeroom)",
    "summary": "Counseling strategy session conducted at LIS Counseling Office (Ext: 213). Reviewed student's GPA of 3.94 and SAT 1530. Recommended submitting Direct Apply applications to Imperial College London and University of Sydney to secure $250 fee waivers, with Early Decision submission to NYU Stern via Common App. Both parents (조기웅 & 정미경) notified via Cialfo Family Portal.",
    "action_items": [
        "Complete Tier 2 course reflection for David Nah (AP Math/Physics) and Peter Yoo (Humanities)",
        "Review full terms for Imperial College London Conditional Offer with Cialfo Guide"
    ]
}

with open("data/student_profile.json", "w", encoding="utf-8") as f:
    json.dump(student_profile, f, indent=2, ensure_ascii=False)
print("Updated student_profile.json with real faculty counselor details!")

# 3. Update lor_requests.json with real recommenders from faculty roster
# Filter real academic secondary teachers
recommender_candidates = [
    {
        "id": "rec-fac-14",
        "teacher_name": "David Nah (나경식)",
        "korean_name": "나경식",
        "english_name": "David Nah",
        "subject": "College Counseling & Advanced Mathematics",
        "department": "College Counseling & Mathematics",
        "extension": "213",
        "status": "In Progress (Teacher Reviewing)",
        "requested_date": "2026-09-30",
        "deadline": "2026-10-28",
        "tier_2_course_reflections": {
            "memorable_project": "Design and telemetry analysis of an autonomous sensor-driven rover for robotics laboratory experiments.",
            "intellectual_growth": "Mastering advanced differential calculations and mathematical modeling to predict physical system behaviors.",
            "link_to_target_major": "Directly foundational for undergraduate Computer Science, Artificial Intelligence, and Quantitative Economics."
        },
        "teacher_submission": {
            "has_submitted": False,
            "input_language": "Korean",
            "draft_status": "Draft v2 in progress"
        }
    },
    {
        "id": "rec-fac-5",
        "teacher_name": "Kyu Mun Hwang (황규문)",
        "korean_name": "황규문",
        "english_name": "Kyu Mun Hwang",
        "subject": "Computer Science & AP Computer Science Principles",
        "department": "Secondary Administration & Technology",
        "extension": "214",
        "status": "Ready for Submission",
        "requested_date": "2026-10-15",
        "deadline": "2026-11-01",
        "tier_2_course_reflections": {
            "memorable_project": "Full-stack web application development and algorithmic graph traversal optimization in Computer Science lab.",
            "intellectual_growth": "Demonstrating exceptional architectural clarity in software design and recursive data structures.",
            "link_to_target_major": "Crucial endorsement for BSc Computing at Imperial College London and NYU Courant Institute."
        },
        "teacher_submission": {
            "has_submitted": False,
            "input_language": "English",
            "draft_status": "Ready for counselor review"
        }
    },
    {
        "id": "rec-fac-4",
        "teacher_name": "Peter Yoo (유찬호)",
        "korean_name": "유찬호",
        "english_name": "Peter Yoo",
        "subject": "Chaplain / H12 Homeroom / Bible & Ethics",
        "department": "Ministry & Senior Homeroom",
        "extension": "",
        "status": "Drafting Request",
        "requested_date": "2026-10-20",
        "deadline": "2026-11-10",
        "tier_2_course_reflections": {
            "memorable_project": "Comparative essay examining post-industrial ethical dilemmas and compassionate leadership in global society.",
            "intellectual_growth": "Demonstrating servant leadership and moral integrity during H12 student council governance.",
            "link_to_target_major": "Highlights character integrity, emotional intelligence, and global citizenship."
        },
        "teacher_submission": {
            "has_submitted": False,
            "input_language": "Korean",
            "draft_status": "Queued"
        }
    }
]

lor_payload = {
    "cap_policy": {
        "max_allowed": 2,
        "requested_count": 2,
        "policy_note": "Leaders International School (LIS) limits formal recommendation requests to 2 secondary faculty members (Principal: Paul Kim, College Counselor: David Nah, Ext: 213).",
        "status": "2 / 2 Recommenders Requested (Cap Reached)"
    },
    "tier_1_common_reflections": {
        "three_adjectives": "Resilient, Analytical, Compassionate",
        "adjectives_explanation": "As an LIS senior, I approach complex technological challenges with quantitative rigor while maintaining genuine empathy for my school community in Ilsan and Paju.",
        "extracurricular_highlights": "LIS Student Council Secretary, Leader of Coding Club, Volunteer tutoring middle school students.",
        "background_challenges": "Balancing rigorous secondary coursework with family responsibilities and active mentorship of younger LIS peers.",
        "auto_sync_enabled": True,
        "last_saved": "2026-10-22 22:34 KST"
    },
    "recommenders": recommender_candidates,
    "available_faculty_recommenders": [
        {"id": f"fac-{f['no']}", "name": f"{f['english_name']} ({f['korean_name']})", "role": f['role'], "ext": f['extension']}
        for f in faculty_list if "TEACHING" in f["division"] or "ADMININSTRATIVE" in f["division"]
    ],
    "multilingual_lor_bridge": {
        "enabled": True,
        "description": "For LIS faculty (e.g. David Nah, Kyu Mun Hwang, Peter Yoo) drafting recommendations in Korean. Gemini AI transforms raw Korean notes into academic admissions English for counselor and headmaster review.",
        "sample_input_language": "Korean",
        "sample_faculty_recommender": "David Nah (나경식 - College Counselor / Math)",
        "sample_raw_teacher_notes": "학생은 LIS 고등부 재학 기간 동안 학업에 매우 성실하고 지적 호기심이 탁월했습니다. 특히 수학과 물리, 컴퓨터 과학 분야에서 뛰어난 분석력을 발휘하며, 실험 오차가 발생했을 때 끈기 있게 원인을 규명하는 과학적 태도를 보였습니다. 급우들을 배려하고 섬기는 리더십 또한 매우 모범적입니다.",
        "ai_converted_english_draft": "\"It is a distinct privilege to recommend this student on behalf of the faculty at Leaders International School. Throughout her academic tenure, she has distinguished herself as a scholar of exceptional intellectual vitality and rigorous analytical integrity. In advanced mathematics, physical sciences, and computing, she demonstrates exemplary perseverance, methodically dissecting discrepancies rather than faltering under empirical challenges. Beyond her scholastic brilliance, she is a humble, compassionate leader who actively uplifts her peers. She epitomizes the highest standards of academic excellence and global leadership.\"",
        "counselor_approval_status": "Approved by David Nah (College Counselor) to cDocs"
    }
}

with open("data/lor_requests.json", "w", encoding="utf-8") as f:
    json.dump(lor_payload, f, indent=2, ensure_ascii=False)
print("Updated lor_requests.json with real LIS faculty recommenders and counselor approval!")
