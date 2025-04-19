import os
import shutil

# Target folder where all organized files will go
target_root = r"C:\Users\gboy1\OneDrive\Documents\All_Files"

# Source folders to search through
source_folders = [
    os.path.join(os.path.expanduser("~"), "Pictures"),
    os.path.join(os.path.expanduser("~"), "Videos"),
    os.path.join(os.path.expanduser("~"), "Downloads"),
    os.path.join(os.path.expanduser("~"), "Documents"),
    os.path.join(os.path.expanduser("~"), "Music"),
]

# File type to category mapping
extensions = {
    ".jpeg": "Images",
    ".jpg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".txt": "Documents",
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".py": "Scripts",
    ".stl": "Models",
}

# Create root target folder if it doesn't exist
os.makedirs(target_root, exist_ok=True)

for folder in source_folders:
    if not os.path.exists(folder):
        print(f"Source folder not found: {folder}")
        continue

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1].lower()

            if extension in extensions:
                category = extensions[extension]
                target_folder = os.path.join(target_root, category)
                os.makedirs(target_folder, exist_ok=True)

                destination_path = os.path.join(target_folder, filename)

                # If file already exists in destination, rename it
                if os.path.exists(destination_path):
                    base, ext = os.path.splitext(filename)
                    counter = 1
                    while os.path.exists(destination_path):
                        new_filename = f"{base}_{counter}{ext}"
                        destination_path = os.path.join(target_folder, new_filename)
                        counter += 1

                shutil.move(file_path, destination_path)
                print(f"Moved {filename} to {category} folder.")
            else:
                print(f"Skipped {filename}. Unknown file extension.")
        else:
            print(f"Skipped {filename}. Not a file.")

print("All files have been organized into All_Files.")
print("File organization complete.")
