#!/bin/bash

# Stop and remove all running Docker containers
docker stop $(docker ps -q) && docker rm $(docker ps -aq)

# Pull and run the new set of Docker images
docker pull your_image_1
docker run -d your_image_1

docker pull your_image_2
docker run -d your_image_2

# Add more pull and run commands as needed for other images

