import shutil
import os

def backup_file(source_path, backup_dir):
    os.makedirs(backup_dir, exist_ok=True)
    shutil.copy(source_path, backup_dir)

if __name__ == "__main__":
    backup_file('important_file.txt', 'backup/')
    print("File backup completed.")
