import sys
import yaml

host = str(sys.argv[1])
user = str(sys.argv[2])
passwd = str(sys.argv[3])
with open('docker-compose.yml') as yml:
    yml_file = yaml.load(yml, Loader=yaml.FullLoader)
    yml_file['services']['db']['environment'][0] = f"MYSQL_DATABASE={host}"
    yml_file['services']['db']['environment'][1] = f"MYSQL_USER={user}"
    yml_file['services']['db']['environment'][2] = f"MYSQL_ROOT_PASSWORD={passwd}"

with open('docker-compose.yml', 'w') as yml:
    yaml.dump(yml_file, yml)
