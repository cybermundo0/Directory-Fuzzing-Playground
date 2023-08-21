from flask import Flask, render_template
import os
import threading
import time
import random
import markdown

app = Flask(__name__)

BASE_DIR = '/app/created_directories/directories'
MAX_DIRECTORIES = 100
WORD_LIST_FILE = 'top_directories.txt'

@app.route('/')
def index():
    with open("README.md", "r") as readme_file:
        content = readme_file.read()
        content_html = markdown.markdown(content)
    return content_html

def create_initial_directories():
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

    for _ in range(30):
        dir_name = str(random.randint(1, 1000))
        os.makedirs(os.path.join(BASE_DIR, dir_name))

def create_directories():
    while True:
        if not os.path.exists(BASE_DIR):
            os.makedirs(BASE_DIR)

        existing_dirs = len(os.listdir(BASE_DIR))
        if existing_dirs >= MAX_DIRECTORIES:
            break

        with open(WORD_LIST_FILE, 'r') as f:
            lines = f.readlines()
            new_dir = random.choice(lines).strip()
            os.makedirs(os.path.join(BASE_DIR, new_dir))

        time.sleep(1800)  # Wait for 30 minutes

@app.route('/<path:directory>')
def show_directory(directory):
    return render_template('directory.html', directory_name=directory)

if __name__ == "__main__":
    threading.Thread(target=create_directories).start()
    create_initial_directories()
    app.run(debug=True,host='0.0.0.0', port=5000)
