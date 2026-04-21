from flask import Flask
import socket
import time

app = Flask(__name__)

@app.route('/process')
def process():
    time.sleep(1)  # simulate work
    return f"Processed by {socket.gethostname()}"

@app.route('/health')
def health():
    return {"status": "ok"}
