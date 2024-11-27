# Use a basic Ubuntu image
FROM ubuntu:20.04

# Install Wine, dependencies, and wget
RUN apt-get update && \
    apt-get install -y wget wine64

# Download the N_m3u8DL-RE.exe (or your required version)
RUN wget https://github.com/rahul0715/jj/blob/main/N_m3u8DL-RE.exe -O /app/N_m3u8DL-RE.exe

# Make the .exe file executable
RUN chmod +x /app/N_m3u8DL-RE.exe

# Set the working directory
WORKDIR /app

# Install any other dependencies for your Python application
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the rest of the application files
COPY . /app/

# Command to run your Python app, or use the entrypoint script
CMD ["python3", "main.py"]
