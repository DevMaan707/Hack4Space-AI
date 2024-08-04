# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Uninstall torch
RUN pip3 uninstall -y torch

# Install torch, torchvision, and torchaudio from the specified index URL
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for Flask
ENV FLASK_APP=app.py

# Run the Flask server
CMD ["flask", "run", "--host=0.0.0.0"]
