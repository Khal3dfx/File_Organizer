# To run the program: python3 File_Organizer.py

import os
import shutil  

# ---------------- CLEAR SCREEN ----------------
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')


# ---------------- FOLDER VALIDATION ----------------
while True:
    clear_screen()
    print("Example of folder's path: /Users/USERNAME/Desktop/TestFolder")

    folder_path = input("Folder to organize: ")

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        print("\n✅ Folder exists, proceeding...")
        print(f"Your folder's path is: {folder_path}")
        input("\nPress Enter to continue...")
        break
    else:
        print("❌ Folder does not exist. Please enter a valid folder path.\n")
        input("\nPress Enter to retry...")


# ---------------- FILE SCANNING ----------------
all_items = os.listdir(folder_path)

# Only files (ignore subfolders)
files = [
    f for f in all_items
    if os.path.isfile(os.path.join(folder_path, f))
]

clear_screen()
print("Files found in folder:\n")
for f in files:
    print("-", f)

input("\nPress Enter to continue...")
clear_screen()


# ---------------- CATEGORY DEFINITIONS ----------------
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov"]
}


# ---------------- FILE → CATEGORY MAPPING ----------------
file_categories = {}

for file in files:
    ext = os.path.splitext(file)[1].lower()
    found = False

    for category, extensions in categories.items():
        if ext in extensions:
            file_categories[file] = category
            found = True
            break

    if not found:
        file_categories[file] = "Others"


# ---------------- PREVIEW MAPPING ----------------
print("Files Mapping:\n")
for file, category in file_categories.items():
    print(f"{file} → {category}")

input("\nPress Enter to continue...")


# ---------------- DRY-RUN SELECTION (NEW) ----------------
while True:
    choice = input("\nRun in dry-run mode? (y/n): ").lower()
    if choice == "y":
        dry_run = True
        print("\n⚠️ Dry-run mode enabled. No files will be moved.")
        break
    elif choice == "n":
        dry_run = False
        print("\n🚀 Actual move mode enabled. Files WILL be moved.")
        break
    else:
        print("❌ Invalid input. Please enter y or n.")


# ---------------- EXECUTION ----------------
if not dry_run:
    # Create destination folders if missing
    for category in ["Images", "Documents", "Videos"]:
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    # Move files
    for file, category in file_categories.items():
        if category in ["Images", "Documents", "Videos"]:
            src = os.path.join(folder_path, file)
            dst = os.path.join(folder_path, category, file)
            shutil.move(src, dst)
            print(f"{file} → {category}/")

    print("\nDone ✅ Files moved successfully.")
else:
    print("\n✅ Dry-run complete. No files were moved.")
