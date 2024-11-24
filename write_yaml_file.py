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