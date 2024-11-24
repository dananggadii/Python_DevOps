#* Monitoring CPU dan RAM Server
#! Memantau penggunaan CPU dan RAM menggunakan psutil
import psutil
import time

def monitor_system(interval):
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory.percent}%")
        print("-" * 30)
        time.sleep(interval)

# Contoh penggunaan
monitor_system(5)