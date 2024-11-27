# Use an official base image
FROM python:3.9-slim

# Set environment variables to avoid tzdata prompt
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York  # Set your desired timezone, e.g., "America/New_York"

# Install tzdata and other dependencies
RUN apt-get update && \
    apt-get install -y tzdata && \
    ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata && \
    apt-get clean

# Other necessary dependencies for your app
RUN apt-get install -y wget

# Copy your application code
COPY . /app

# Set the working directory
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose any necessary ports
EXPOSE 80

# Define the command to run your bot
CMD ["python", "main.py"]
