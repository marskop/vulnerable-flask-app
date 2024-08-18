# Use a lightweight Python image
FROM python:3.8-slim

# Install git
RUN apt-get update && apt-get install -y git

# Upgrade pip and install necessary packages
RUN pip install --upgrade pip
RUN pip install bandit semgrep trufflehog sqlmap

# Set the working directory to /app inside the container
WORKDIR /app

# Copy only the contents of the app/ directory to /app in the container
COPY ./app /app

# Default command to run when the container starts
CMD ["/bin/bash"]
