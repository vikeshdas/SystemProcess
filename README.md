# SystemProcess

This project is a Django-based web application designed to monitor and display all running processes and programs on the host system. The application features a backend for retrieving process details and a user-friendly frontend for visualization. It is Dockerized for easy deployment and platform

### Displays system processes with the following details
- Process ID (PID)
- Process Name
- User Running the Process
- CPU Usage (%)
- Memory Usage (MB)
- Start Time

### Features include
- Search/Filter: Find specific processes by process ID,Name,User,CPU Usage,Memory Usage,Start Time.

- Sort: User can sort process by process ID,Name,User,CPU Usage,Memory Usage,Start Time .

## Step to run project without docker container
- git clone https://github.com/vikeshdas/SystemProcess.git

- conda create -n env_name python=3.10

- activate conda envirement

- got the directory of the project where requirement.txt file exist and run pip install -r requirements.txt

- run command python manage.py runserver

## Step to run Project in Docker container

- git clone https://github.com/vikeshdas/SystemProcess.git
- Oper CMD and go to the directory of the project where Dockerfile exist.
- Create docker image from Dockerfile : Run command  docker build -t web_image -f Dockerfile .
- Run command docker compose up web_service to run project in container.
