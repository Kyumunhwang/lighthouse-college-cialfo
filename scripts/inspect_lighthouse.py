import sqlite3
import json
from pathlib import Path

db_path = Path("temp_lighthouse/lccs.db")
conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in lccs.db:", [t["name"] for t in tables])

for t in tables:
    t_name = t["name"]
    cursor.execute(f"SELECT COUNT(*) as cnt FROM [{t_name}];")
    cnt = cursor.fetchone()["cnt"]
    cursor.execute(f"PRAGMA table_info([{t_name}]);")
    cols = cursor.fetchall()
    col_names = [c["name"] for c in cols]
    print(f"Table [{t_name}]: {cnt} rows | Cols: {col_names}")

# Let's inspect colleges/universities table specifically
for t in tables:
    t_name = t["name"]
    if "college" in t_name.lower() or "univ" in t_name.lower() or "school" in t_name.lower():
        cursor.execute(f"SELECT * FROM [{t_name}] LIMIT 3;")
        sample = [dict(r) for r in cursor.fetchall()]
        print(f"\nSample from [{t_name}]:")
        for s in sample:
            print(s)
