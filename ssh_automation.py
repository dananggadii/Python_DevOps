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