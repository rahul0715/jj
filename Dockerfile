FROM ubuntu:20.04

# Install dependencies
RUN apt-get update && \
    apt-get install -y wget tar && \
    apt-get install -y wine64

# Download and extract N_m3u8DL-RE
RUN wget https://github.com/nilaoda/N_m3u8DL-RE/releases/download/v0.2.1-beta/N_m3u8DL-RE_Beta_linux-x64_20240828.tar.gz && \
    tar -xvzf N_m3u8DL-RE_Beta_linux-x64_20240828.tar.gz && \
    chmod +x N_m3u8DL-RE mp4decrypt

# Copy your project files into the container
COPY . /app/

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Command to run your application
CMD ["python3", "main.py"]
