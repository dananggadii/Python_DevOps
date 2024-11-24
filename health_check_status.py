# Monitoring Status Layanan (Health Check)
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