# combined_tasks_terminal.py

# ---------------- Task 1 ----------------
print("Task 1 running")
# Example Task1 code
print("Task 1 done\n")

# ---------------- Task 2 ----------------
print("Task 2 running")
# Example Task2 code
print("Task 2 done\n")

# ---------------- Task 3 ----------------
print("Task 3 running (Flask simulation)")

from flask import Flask
import threading
import requests
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Task 3 Flask app running"

def run_flask():
    app.run(debug=False, port=5000)

# Start Flask server in background thread
flask_thread = threading.Thread(target=run_flask)
flask_thread.daemon = True
flask_thread.start()

# Wait a bit for Flask server to start
time.sleep(1)

# Make a GET request to Flask server and print output in terminal
try:
    response = requests.get("http://127.0.0.1:5000/")
    print("Task 3 output:", response.text, "\n")
except Exception as e:
    print("Task 3 request failed:", e, "\n")

# ---------------- Task 4 ----------------
print("Task 4 running")
def square(x):
    return x * x

nums = [1, 2, 3, 4, 5]
squares = [square(n) for n in nums]
print("Squares:", squares)
print("Task 4 done\n")

# Stop the script
print("All tasks completed!")
