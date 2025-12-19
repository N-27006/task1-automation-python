import os
import logging

# Configure logging
logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def rename_files(folder_path):
    try:
        files = os.listdir(folder_path)
        count = 1

        logging.info("File renaming started")

        for file in files:
            old_path = os.path.join(folder_path, file)

            if os.path.isfile(old_path):
                new_name = f"document_{count}.txt"
                new_path = os.path.join(folder_path, new_name)

                os.rename(old_path, new_path)
                print(f"Renamed: {file} → {new_name}")
                logging.info(f"Renamed {file} to {new_name}")

                count += 1

        print("\n✅ Automation completed successfully!")
        logging.info("File renaming completed successfully")

    except Exception as e:
        print("❌ Error occurred:", e)
        logging.error(f"Error occurred: {e}")


if __name__ == "__main__":
    folder = input("Enter folder path to rename files: ")
    rename_files(folder)

