FROM ubuntu:latest

# Install cron and other dependencies
RUN apt-get update && apt-get install -y cron docker.io && rm -rf /var/lib/apt/lists/*

COPY update_containers.sh /usr/src/app/
WORKDIR /usr/src/app

RUN chmod +x update_containers.sh

# Create the cron log file
RUN touch /var/log/cron.log

# Add cron job to run immediately and then every 8 hours
RUN echo "@reboot /usr/src/app/update_containers.sh >> /var/log/cron.log 2>&1" | crontab -

# Run cron in the foreground when the container starts
CMD cron && tail -f /var/log/cron.log
