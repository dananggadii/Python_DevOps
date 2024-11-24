print("Python for DevOps")

#* Monitoring Status Layanan (Health Check)
#! Mengecek apakah sebuah layanan berjalan dengan HTTP 200 OK.
import requests

def check_service_health(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"Service at {url} is UP!")
        else:
            print(f"Service at {url} is DOWN! Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to {url}: {e}")

# Contoh penggunaan
check_service_health("https://example.com")

# ----------------------------------------------------------------------------------------------------------------------

#* Automasi SSH untuk Menjalankan Perintah Jarak Jauh
#! Menggunakan paramiko untuk mengelola server melalui SSH.
import paramiko

def execute_remote_command(host, username, password, command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=username, password=password)

        stdin, stdout, stderr = ssh.exec_command(command)
        print(f"Output:\n{stdout.read().decode()}")
        print(f"Errors:\n{stderr.read().decode()}")

        ssh.close()
    except Exception as e:
        print(f"SSH Connection Error: {e}")

# Contoh penggunaan
execute_remote_command("192.168.1.10", "user", "password", "ls -la /var/log")

# ----------------------------------------------------------------------------------------------------------------------

#* Membaca dan Menulis File YAML
#! Manipulasi file konfigurasi seperti YAML.
import yaml

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def write_yaml(file_path, data):
    with open(file_path, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

# Contoh penggunaan
config = read_yaml("config.yaml")
print(config)

config['new_key'] = 'new_value'
write_yaml("updated_config.yaml", config)

# ----------------------------------------------------------------------------------------------------------------------

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

# ----------------------------------------------------------------------------------------------------------------------

#* Menggunakan AWS SDK (Boto3) untuk Mengelola S3
#! Mengunggah file ke bucket S3.
import boto3

def upload_to_s3(bucket_name, file_path, object_name=None):
    s3 = boto3.client('s3')
    if object_name is None:
        object_name = os.path.basename(file_path)
    
    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print(f"File {file_path} uploaded to {bucket_name}/{object_name}")
    except Exception as e:
        print(f"Failed to upload file: {e}")

# Contoh penggunaan
upload_to_s3("my-bucket", "test.txt")

# ----------------------------------------------------------------------------------------------------------------------

#* Mengelola Docker Container
#! Menggunakan pustaka docker-py untuk menjalankan container.
import docker

def create_and_run_container(image, name):
    client = docker.from_env()
    try:
        container = client.containers.run(image, name=name, detach=True)
        print(f"Container {name} started with ID: {container.id}")
    except Exception as e:
        print(f"Failed to start container: {e}")

# Contoh penggunaan
create_and_run_container("nginx:latest", "my-nginx-container")

# ----------------------------------------------------------------------------------------------------------------------

#* Menjalankan Command Shell
#! Menggunakan subprocess untuk menjalankan perintah shell.
import subprocess

def run_shell_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(f"Command Output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error:\n{e.stderr}")

# Contoh penggunaan
run_shell_command("systemctl status nginx")

# ----------------------------------------------------------------------------------------------------------------------

#* Men-deploy Aplikasi dengan Ansible
#! Contoh skrip Python untuk menjalankan playbook Ansible menggunakan library ansible-runner.
import ansible_runner

def run_ansible_playbook(playbook_path, inventory_path):
    try:
        runner = ansible_runner.run(
            playbook=playbook_path,
            inventory=inventory_path
        )
        if runner.rc == 0:
            print("Playbook executed successfully!")
        else:
            print("Playbook execution failed!")
        print(f"Stdout: {runner.stdout.read()}")
    except Exception as e:
        print(f"Error running playbook: {e}")

# Contoh penggunaan
run_ansible_playbook("site.yml", "inventory.ini")

# ----------------------------------------------------------------------------------------------------------------------

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

# ----------------------------------------------------------------------------------------------------------------------

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
