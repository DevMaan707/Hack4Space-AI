# Dockerfile

FROM python:3.9-slim

WORKDIR /app

# Copy the application code
COPY . /app

# Create a virtual environment
RUN python3 -m venv venv

# Activate the virtual environment and install dependencies
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt
RUN . venv/bin/activate && pip install gunicorn


# Expose the application port
EXPOSE 5000

# Set the entrypoint to activate the virtual environment and run gunicorn
CMD ["/bin/bash", "-c", ". venv/bin/activate && gunicorn --bind 0.0.0.0:5000 app:app"]
