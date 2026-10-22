import openpyxl
import json
from pathlib import Path

excel_path = Path("Faculty Roster.xlsx")
wb = openpyxl.load_workbook(excel_path, data_only=True)
sheet = wb["2026 Fall"]

faculty_list = []

for r in range(4, sheet.max_row + 1):
    vals = [cell.value for cell in sheet[r]]
    if not any(vals):
        continue
    no = vals[1]
    emp = vals[2]
    div = vals[3]
    hire_date = vals[4]
    k_name = vals[5]
    eng_name = vals[6]
    dob = vals[7]
    role = vals[8]
    ext = vals[9]
    
    if (k_name or eng_name) and str(k_name).strip() != "None":
        item = {
            "no": no,
            "employment": str(emp).strip() if emp else "Full-Time",
            "division": str(div).strip() if div else "",
            "korean_name": str(k_name).strip() if k_name else "",
            "english_name": str(eng_name).strip() if eng_name else "",
            "display_name": f"{eng_name} ({k_name})" if eng_name and k_name else (k_name or eng_name),
            "role": str(role).strip().replace('\n', ' / ') if role else "",
            "extension": str(ext).strip() if ext else ""
        }
        faculty_list.append(item)

print(f"Total faculty members: {len(faculty_list)}")
with open("data/lis_faculty.json", "w", encoding="utf-8") as f:
    json.dump(faculty_list, f, indent=2, ensure_ascii=False)

for f in faculty_list:
    print(f"No.{f['no']} | {f['korean_name']} ({f['english_name']}) | Role: {f['role']} | Ext: {f['extension']}")
