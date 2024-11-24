#* Membersihkan File Log Lama
#! Menghapus file log yang lebih lama dari 7 hari di direktori tertentu. 
import os
import time

def clean_old_logs(directory, days):
    now = time.time()
    cutoff = now - (days * 86400)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and os.path.getmtime(file_path) < cutoff:
            os.remove(file_path)
            print(f"Deleted: {file_path}")

# Contoh penggunaan
clean_old_logs("/var/log/myapp", 7)