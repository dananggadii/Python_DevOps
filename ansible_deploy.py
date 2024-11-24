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