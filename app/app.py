from flask import Flask, render_template
import os
import threading
import time
import random

app = Flask(__name__)

# Path to the directory where directories will be created
BASE_DIR = '/app/created_directories'
# File that contains a list of directory names
WORD_LIST = 'top_directories.txt'


# Serve the main page that provides the context about the app.
# This is the landing page that users will see when they access the root URL.
@app.route('/')
def main_page():
    return render_template('index.html')

# List the directories that have been created.
# This is a hidden route not explicitly mentioned in the main page, intended for users to discover through fuzzing.
@app.route('/hidden/')
def hidden_directories():
    directories = os.listdir(BASE_DIR)
    return render_template('directories.html', directories=directories)

# Serve a static page for the specified directory.
# If a directory matching the provided dirname exists, serve a static page for it. Otherwise, return a 404 error.
@app.route('/<dirname>')
def directory_page(dirname):
    # Check if the directory exists
    dir_path = os.path.join(BASE_DIR, dirname)
    if os.path.exists(dir_path):
        return f"Welcome to the static page for {dirname}!"
    else:
        return "Directory not found.", 404

# Create the initial 30 directories inside the BASE_DIR.
# This function is called once when the app starts to set up the directory environment.
def create_initial_directories():
    # Check if the word list exists
    if not os.path.exists(WORD_LIST):
        raise FileNotFoundError(f"Word list '{WORD_LIST}' not found.")
    
    # Read directory names from the word list
    with open(WORD_LIST, 'r') as file:
        lines = file.readlines()
        directory_names = random.sample(lines, 30)
    
    # Create each directory from the list
    for directory in directory_names:
        os.makedirs(os.path.join(BASE_DIR, directory.strip()), exist_ok=True)

# Periodically create a new directory every 30 minutes.
# Stop creating new directories after a total of 100 directories have been created. This function is run in a separate thread.
def periodic_directory_creation():
    while True:
        # Sleep for 30 minutes
        time.sleep(1800)
        
        # Get the number of existing directories
        existing_dirs = len(os.listdir(BASE_DIR))
        
        # If there are 100 directories, stop creating more
        if existing_dirs >= 100:
            break

        # Select a random directory name from the word list
        with open(WORD_LIST, 'r') as file:
            directory_name = random.choice(file.readlines()).strip()
        
        # Create the directory
        os.makedirs(os.path.join(BASE_DIR, directory_name), exist_ok=True)

# When the app starts, setup the directory environment
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)
create_initial_directories()

# Start the periodic directory creation in a separate thread
threading.Thread(target=periodic_directory_creation).start()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
