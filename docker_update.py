import sys

secret = str(sys.argv[1])
host = str(sys.argv[2])
user = str(sys.argv[3])
passwd = str(sys.argv[4])
with open('Dockerfile', 'a') as docker:
    docker.write(f'ENV SECRET_KEY={secret} \n')
    docker.write(f'ENV MYSQL_DATABASE={host} \n')
    docker.write(f'ENV MYSQL_USER={user} \n')
    docker.write(f'ENV MYSQL_ROOT_PASSWORD={passwd} \n')
