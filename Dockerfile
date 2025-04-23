# Use the official lightweight Python image
FROM python:3.12-slim

# Prevent Python from writing .pyc files to ensure that the containner remains lean and consistent 
ENV PYTHONDONTWRITEBYTECODE=1
#Enable unbuffered output to see logs in real time
ENV PYTHONUNBUFFERED=1

# Install system dependencies for Selenium & Chrome
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    gnupg \
    unzip \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
 && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" \
      > /etc/apt/sources.list.d/google-chrome.list \
 && apt-get update && apt-get install -y google-chrome-stable \
 && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy application code
COPY src/ src/

# Create folder for downloaded spreadsheets
RUN mkdir -p downloads

# Command to run the app
ENTRYPOINT ["python", "-m", "src"]
