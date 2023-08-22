# My Flask App: Directory Fuzzing Playground

Welcome to this unique Flask application. At its heart, it's more than just a simple web application that creates directories. This repository is a testament to the journey of learning and improving web security techniques, particularly directory fuzzing.

### The Why Behind The App
With the increasing complexity of web applications, it's ever more crucial to ensure every nook and cranny of a web app is secure. One of the often overlooked aspects of web security is unprotected directories and endpoints. Unwanted exposure can lead to potential vulnerabilities, and that's where directory fuzzing comes into play. Directory fuzzing is a technique used by security experts to discover potential security flaws by locating unprotected directories or endpoints.

### What Does This App Do?
This application starts by creating 30 directories. But it doesn't stop there. Every 30 minutes, a new directory comes to life, adding a layer of dynamism. This functionality serves two core purposes:

1. **Continuous Learning**: As new directories pop up, it offers a fresh challenge for those honing their fuzzing skills.
2. **Automation in Fuzzing**: This ever-evolving landscape is perfect for those looking to automate their fuzzing techniques. Imagine setting up an alert system that notifies you every time a new endpoint is discovered. It's not just about finding directories; it's about automating responses to such discoveries.

### Dockerized for Flexibility
Understanding the diverse environments security professionals work in, this app is containerized using Docker. Whether you're running a Windows machine, a Mac, or a Linux distribution, Docker ensures this application can be spun up locally, offering a consistent testing ground for your fuzzing experiments.

So, whether you're a seasoned security expert or someone just starting with fuzzing, this application aims to be your playground, your challenge, and most importantly, a step towards making the web a safer place.

---

Feel free to add or modify any part of this description to make it more aligned with your vision or objective for the app.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/): Ensure Docker is installed on your system.

## Directory Structure

```
Directory-Fuzzing-Playground/
│
├── app/
│   ├── created_directories/  # This directory will get populated with new directories over time.
│   │
│   ├── static/
│   │   └── css/
│   │       └── styles.css    # Optional, in case you want to include some custom styles.
│   │
│   ├── templates/
│   │   └── index.html        # The template for the main directory page.
│   │
│   ├── app.py                # Main Flask application file.
│   │
│   └── top_directories.txt   # Contains the list of directory names.
│
├── Dockerfile
│
└── requirements.txt          # Contains all the Python package dependencies.

```

## Building and Running the Docker Container

1. **Navigate to your project directory**:
   
   Open a terminal or command prompt and navigate to the Flask application's root directory (`/my_flask_app/`):

   ```bash
   cd /path/to/my_flask_app/
   ```

   Replace `/path/to/` with the appropriate path to your Flask app.

2. **Build the Docker Image**:
   
   From within the `/my_flask_app/` directory, run:

   ```bash
   docker build -t myflaskapp:latest .
   ```

   This command will build a Docker image from the `Dockerfile` in the current directory and tag it with the name `myflaskapp` and version `latest`.

3. **Run the Docker Container**:

   Start a Docker container from the `myflaskapp:latest` image:

   ```bash
   docker run -p 5001:5001 myflaskapp:latest
   ```

   You can then access the Flask app at `http://localhost:5000` on your local machine's web browser.

4. **Stopping the Docker Container**:

   - Press `CTRL+C` in the terminal where the container is running.
   - Alternatively, you can use the `docker ps` command to list running containers, find the container ID of your app, and then use `docker stop [CONTAINER_ID]` to stop it.
