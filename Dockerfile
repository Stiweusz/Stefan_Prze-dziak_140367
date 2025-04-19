# Use official Python base image
FROM python:3.11-slim-buster

# Set working directory in container
WORKDIR /app

# Copy requirements and install
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY app.py .

# Set environment variable for Flask
ENV FLASK_APP=app
ENV FLASK_RUN_PORT=5000

# Expose port for external access
EXPOSE 5000

# Run Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
