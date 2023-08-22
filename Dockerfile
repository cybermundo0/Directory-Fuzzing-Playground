# Use an official Python runtime as the parent image
FROM python:3.8-slim-bullseye

# Set working directory
WORKDIR /app

# Copy your code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Adjust permissions for /app and its subdirectories
RUN chown -R nobody:nogroup /app

# Expose the port your app runs on
EXPOSE 5001

# Run gunicorn or your preferred server as root
CMD ["gunicorn", "app.app:app", "--bind", "0.0.0.0:5001", "--user", "nobody"]