# Use an official Python runtime as the parent image
FROM python:3.8-slim-bullseye

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app/app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Switching to a non-root user
RUN useradd -m appuser && mkdir -p /app/created_directories && chown -R appuser:appuser /app
USER appuser

# Copy the current directory contents into the container at /app
COPY --chown=appuser:appuser . .

# Run app.py when the container launches
CMD ["gunicorn", "app.app:app", "-b", "0.0.0.0:5001"]
