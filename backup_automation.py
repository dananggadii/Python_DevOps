#* Backup File Otomatis
#! Membuat backup dari direktori tertentu.
import os
import shutil
from datetime import datetime

def backup_directory(source_dir, backup_dir):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    destination = os.path.join(backup_dir, f"backup_{timestamp}")
    shutil.copytree(source_dir, destination)
    print(f"Backup completed: {destination}")

# Contoh penggunaan
backup_directory("/var/www/html", "/backups")