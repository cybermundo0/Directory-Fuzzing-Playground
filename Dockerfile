# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create a new user "appuser" and set it as the current user
RUN useradd -m appuser
USER appuser

# Install the required packages as root
USER root
RUN pip install --no-cache-dir -r requirements.txt

# Switch back to appuser
USER appuser

# Make port 5000 available to the outside world
EXPOSE 5000

# Define the environment in production mode
ENV FLASK_ENV=production

# Run the app when the container starts
CMD ["python", "./app.py"]
