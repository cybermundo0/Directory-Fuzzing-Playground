from flask import Flask, render_template
import os
import threading
import time
import random

app = Flask(__name__)

# Base directory where we want to create the folders
BASE_DIR = os.path.join(os.getcwd(), "created_directories", "directories")

@app.route('/')
def index():
    dirs = os.listdir(BASE_DIR)
    return render_template('index.html', dirs=dirs)

@app.route('/directory/<dirname>')
def directory_page(dirname):
    return render_template('directory.html', dirname=dirname)

def get_random_word():
    with open('top_directories.txt', 'r') as file:
        words = file.readlines()
    return random.choice(words).strip()

def create_directory(name):
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)  # Use makedirs to create any missing intermediate directories
    path = os.path.join(BASE_DIR, name)
    if not os.path.exists(path):
        os.mkdir(path)

def create_directories():
    existing_dirs = len(os.listdir(BASE_DIR))
    max_directories = 100

    # Create up to 30 directories initially if none exist
    for i in range(existing_dirs, existing_dirs + 30):
        if i >= max_directories:
            return
        create_directory(f"dir_{i}")

    i = existing_dirs + 30

    # Continue creating new directories every 30 minutes using a random word until we reach the maximum
    while i < max_directories:
        time.sleep(1800)  # 1800 seconds is 30 minutes
        create_directory(get_random_word())
        i += 1

# Running the create_directories function in a background thread
t = threading.Thread(target=create_directories)
t.start()

if __name__ == "__main__":
    app.run(debug=True)