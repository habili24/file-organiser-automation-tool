import os
import shutil

# Folder where the script is running
BASE_DIR = os.getcwd()

# File type rules
FILE_TYPES = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"]
}

def organize_files():
    for filename in os.listdir(BASE_DIR):

        file_path = os.path.join(BASE_DIR, filename)

        # Skip folders and the script itself
        if os.path.isdir(file_path) or filename == "file_organizer.py":
            continue

        moved = False

        for folder, extensions in FILE_TYPES.items():
            if filename.lower().endswith(tuple(extensions)):
                destination = os.path.join(BASE_DIR, folder)
                os.makedirs(destination, exist_ok=True)
                shutil.move(file_path, os.path.join(destination, filename))
                print(f"Moved {filename} → {folder}")
                moved = True
                break

        if not moved:
            other_folder = os.path.join(BASE_DIR, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved {filename} → Others")

if __name__ == "__main__":
    organize_files()
    print("\n✅ File organization complete.")
