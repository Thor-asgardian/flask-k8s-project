from flask import Flask
import requests
import socket

app = Flask(__name__)

@app.route('/')
def home():
    try:
        res = requests.get("http://app2-service:6000/process")
        return f"""
        <h2>App1 (Frontend)</h2>
        <p>Hostname: {socket.gethostname()}</p>
        <p>Response from App2: {res.text}</p>
        """
    except:
        return "App2 not reachable"

@app.route('/health')
def health():
    return {"status": "ok"}
