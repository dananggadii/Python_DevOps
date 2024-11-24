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