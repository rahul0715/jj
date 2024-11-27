# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables to prevent tzdata interactive prompts
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York  # Change to your desired timezone (e.g., "Europe/London")

# Install necessary packages and configure the timezone
RUN apt-get update && \
    apt-get install -y tzdata wget && \
    ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata && \
    apt-get clean

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Expose any necessary ports (if your app needs to listen on a port)
EXPOSE 80

# Define the command to run your app (assuming the entry point is main.py)
CMD ["python", "main.py"]
