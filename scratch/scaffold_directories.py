import os

days = ["day 1", "day 2", "day 3", "day 4", "day 5", "day 6", "day 7"]
subfolders = [
    "data/raw",
    "data/processed",
    "data/db",
    "notebooks",
    "sql",
    "dashboard",
    "reports/charts",
    "scripts"
]

project_root = r"c:\Users\jibum\OneDrive\Desktop\Bluestock Internship"

for day in days:
    day_path = os.path.join(project_root, day)
    print(f"Scaffolding {day}...")
    for sub in subfolders:
        path = os.path.join(day_path, sub)
        os.makedirs(path, exist_ok=True)
        print(f"  Created: {path}")

print("Scaffolding complete!")
