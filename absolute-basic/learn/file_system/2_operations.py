# Operations
import shutil
from pathlib import Path

print("-----------Creating------------\n")
## 1. create a directory
notes_dir = Path.cwd() / "notes"
print(f"{notes_dir} exists: {notes_dir.exists()}")

if not notes_dir.exists():
    notes_dir.mkdir()
    print(f"{notes_dir} created")
else:
    print(f"{notes_dir} already exists")

print("--------------------------------\n")
## 2. create a subdirectory
monthly_dir = notes_dir / "plans" / "monthly"
print(f"{monthly_dir} exists: {monthly_dir.exists()}")
if not monthly_dir.exists():
    monthly_dir.mkdir(parents=True)  # create the directory and all parent directories
    print(f"{monthly_dir} created")
else:
    print(f"{monthly_dir} already exists")

weekly_dir = notes_dir / "plans" / "weekly"
print(f"{weekly_dir} exists: {weekly_dir.exists()}")
weekly_dir.mkdir(parents=True, exist_ok=True)

print("--------------------------------\n")
## 3 create a file
january_plan_file = monthly_dir / "january.txt"
print(f"{january_plan_file} exists: {january_plan_file.exists()}")
if not january_plan_file.exists():
    print(
        f"before creating {january_plan_file} is a file: {january_plan_file.is_file()}"
    )
    january_plan_file.touch()
    print(f"{january_plan_file} created")
    print(
        f"after creating {january_plan_file} is a file: {january_plan_file.is_file()}"
    )
else:
    print(f"{january_plan_file} already exists")

year_plan_file = notes_dir / "plans" / "yearly" / "2026.txt"
print(f"{year_plan_file} exists: {year_plan_file.exists()}")
if not year_plan_file.exists():
    year_plan_file.parent.mkdir(parents=True, exist_ok=True)
    year_plan_file.touch()
    print(f"{year_plan_file} created")
else:
    print(f"{year_plan_file} already exists")

print("--------------------------------\n")
print("-----------Iterating------------")
plans_dir = notes_dir / "plans"
readme_plans = plans_dir / "README.md"
readme_plans.touch()
for path in plans_dir.iterdir():
    print(f"path: {path}")

print("--------------------------------\n")
print("-----------Searching------------")
for path in notes_dir.glob("**/*.txt"):
    print(f"path: {path}")

for path in notes_dir.glob("**/*.md"):
    print(f"path: {path}")

print("--------------------------------\n")
print("-----------Searching with wildcards------------")

paths = [
    notes_dir / "goal1.txt",
    notes_dir / "goal2.txt",
    notes_dir / "plans" / "yearly" / "2028.txt",
    notes_dir / "plans" / "yearly" / "2027.txt",
    notes_dir / "plans" / "goal3.txt",
    notes_dir / "plans" / "monthly" / "january.txt",
    notes_dir / "plans" / "monthly" / "february.md",
    notes_dir / "plans" / "monthly" / "march.txt",
    notes_dir / "plans" / "monthly" / "april.md",
    notes_dir / "plans" / "monthly" / "may.txt",
    notes_dir / "plans" / "monthly" / "june.md",
    notes_dir / "plans" / "monthly" / "july.txt",
    notes_dir / "plans" / "monthly" / "august.md",
    notes_dir / "plans" / "monthly" / "september.txt",
    notes_dir / "plans" / "monthly" / "october.md",
    notes_dir / "plans" / "monthly" / "november.txt",
    notes_dir / "plans" / "monthly" / "december.md",
]
for path in paths:
    path.touch()

## Searching with wildcards
notes_txt_files = list(notes_dir.glob("**/*.txt"))
for file in notes_txt_files:
    print(f"txt file: {file}")

yearly_dir = notes_dir / "plans" / "yearly"
yearly_files = yearly_dir.glob("202*.txt")
for file in yearly_files:
    print(f"yearly file: {file}")

## ? wildcard
goal_files = notes_dir.glob("**/goal?.txt")
for file in goal_files:
    print(f"goal file: {file}")

## [] wildcard
odd_goal_files = notes_dir.glob("**/goal[13579].txt")
for file in odd_goal_files:
    print(f"odd goal file: {file}")

l_s_files = notes_dir.glob("**/*[ls]*.*")
for file in l_s_files:
    print(f"l or s file: {file}")

print("--------------------------------\n")
print("-----------Moving and Deleting------------")
# Moving a file
old_path_goal3 = notes_dir / "plans" / "goal3.txt"
new_path_goal3 = notes_dir / "goal3.txt"
old_path_goal3.replace(new_path_goal3)

print(f"old path goal3 exists: {old_path_goal3.exists()}")
print(f"new path goal3 exists: {new_path_goal3.exists()}")

## Moving a directory
source_dir = notes_dir / "plans" / "yearly"
target_dir = notes_dir / "yearly_plans"
# source_dir.replace(target_dir)

print(f"source dir exists: {source_dir.exists()}")
print(f"target dir exists: {target_dir.exists()}")

## Deleting a file
file_to_delete = notes_dir / "goal3.txt"
file_to_delete.unlink(missing_ok=True)
print(f"file to delete exists: {file_to_delete.exists()}")

## Deleting a directory
empty_dir_to_delete = notes_dir / "plans" / "weekly"
if empty_dir_to_delete.exists():
    empty_dir_to_delete.rmdir()
    print(f"empty dir to delete exists: {empty_dir_to_delete.exists()}")
else:
    print(f"empty dir to delete does not exist")

## Deleting a directory and all its contents
if notes_dir.exists():
    shutil.rmtree(notes_dir)
    print(f"notes dir exists: {notes_dir.exists()}")
else:
    print(f"notes dir does not exist")
