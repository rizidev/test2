🚀 My First Docker App

This is a simple project to learn Docker, GitHub, and DockerHub integration. The app is containerized using Docker and deployed on DockerHub.

📦 Features

Containerized application with Docker

Easy build and run steps

Published to DockerHub

⚙️ Prerequisites

Docker
 installed

Git
 installed

DockerHub account

🛠️ Build the Docker Image
docker build -t rizidev/my_firs:latest .

📤 Push to DockerHub
docker login
docker push rizidev/my_firs:latest

▶️ Run the Container
docker run -d -p 8080:8080 rizidev/my_firs:latest


The app will be available at:
👉 http://localhost:8080

🔗 DockerHub Image

You can pull the image directly:

docker pull rizidev/my_firs:latest

📖 Notes

Replace rizidev/my_firs with your own repo name if changed.

Make sure Docker Desktop is running when using docker run.
