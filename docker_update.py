import sys

secret = str(sys.argv[1])
host = str(sys.argv[2])
user = str(sys.argv[3])
passwd = str(sys.argv[4])
with open('Dockerfile', 'a') as docker:
    docker.write(f'ENV SECRET_KEY={secret} \n')
    docker.write(f'ENV DB_NAME={host} \n')
    docker.write(f'ENV DB_USER={user} \n')
    docker.write(f'ENV DB_PASSWORD={passwd} \n')
    docker.write(f'RUN python crm/manage.py collectstatic --no-input \n')
    docker.write(f'RUN chmod -R 775 static')
