import os
import shutil
import logging

# ---------------- LOG CONFIG ----------------
logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- FUNCTIONS ----------------
def rename_files(folder_path):
    try:
        for file in os.listdir(folder_path):
            old_path = os.path.join(folder_path, file)

            if os.path.isfile(old_path):
                new_name = file.lower().replace(" ", "_")
                new_path = os.path.join(folder_path, new_name)

                os.rename(old_path, new_path)
                logging.info(f"Renamed: {file} → {new_name}")
    except Exception as e:
        logging.error(f"Rename Error: {e}")

def sort_files(folder_path):
    try:
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)

            if os.path.isfile(file_path):
                ext = file.split(".")[-1]

                ext_folder = os.path.join(folder_path, ext.upper() + "_FILES")

                if not os.path.exists(ext_folder):
                    os.mkdir(ext_folder)

                shutil.move(file_path, ext_folder)
                logging.info(f"Moved {file} to {ext_folder}")
    except Exception as e:
        logging.error(f"Sort Error: {e}")

def clean_empty_folders(folder_path):
    try:
        for root, dirs, files in os.walk(folder_path):
            for d in dirs:
                dir_path = os.path.join(root, d)
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)
                    logging.info(f"Removed empty folder: {dir_path}")
    except Exception as e:
        logging.error(f"Clean Error: {e}")

# ---------------- MAIN ----------------
if __name__ == "__main__":
    folder_path = input("Enter folder path: ")

    if not os.path.exists(folder_path):
        print("❌ Invalid path")
    else:
        rename_files(folder_path)
        sort_files(folder_path)
        clean_empty_folders(folder_path)

        print("✅ Automation Completed Successfully!")
