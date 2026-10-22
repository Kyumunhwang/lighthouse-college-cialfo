import openpyxl
import json
from pathlib import Path

excel_path = Path("2026 Fall Semester LIS Student Roster.xlsx")
wb = openpyxl.load_workbook(excel_path, data_only=True)
sheet = wb["International"]

cur_section = ""
cur_teacher = ""

all_students = []

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
    father = vals[12] if len(vals) > 12 else None
    mother = vals[13] if len(vals) > 13 else None
    cell_phone = vals[15] if len(vals) > 15 else None
    remarks = vals[19] if len(vals) > 19 else None
    
    if k_name and stu_id:
        student = {
            "row": r,
            "section": cur_section,
            "homeroom_teacher": cur_teacher,
            "korean_name": str(k_name).strip(),
            "passport_name": str(passport_name).strip() if passport_name else "",
            "english_name": str(eng_name).strip() if eng_name else "",
            "student_id": str(stu_id).strip(),
            "grade": grade_val,
            "dob": str(dob).strip() if dob else "",
            "gender": str(gender).strip() if gender else "",
            "address": str(address).strip() if address else "",
            "father": str(father).strip() if father else "",
            "mother": str(mother).strip() if mother else "",
            "cell": str(cell_phone).strip() if cell_phone else "",
            "remarks": str(remarks).strip() if remarks else ""
        }
        all_students.append(student)

print(f"Total students parsed: {len(all_students)}")
with open("data/lis_all_students.json", "w", encoding="utf-8") as f:
    json.dump(all_students, f, indent=2, ensure_ascii=False)

# Breakdown by section
sections = {}
for s in all_students:
    sec = s["section"]
    sections[sec] = sections.get(sec, [])
    sections[sec].append(s)

for sec, slist in sections.items():
    print(f"Section {sec} (Homeroom: {slist[0]['homeroom_teacher']}): {len(slist)} students")

print("\nH12 Seniors:")
for s in sections.get("H12 (17)", []):
    print(f"- {s['student_id']}: {s['korean_name']} ({s['passport_name']} / {s['english_name']}) | Parents: {s['father']}, {s['mother']} | Homeroom: {s['homeroom_teacher']}")
