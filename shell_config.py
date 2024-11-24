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