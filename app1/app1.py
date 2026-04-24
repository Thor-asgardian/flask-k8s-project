from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"app": "app1", "message": "Hello from App1"})

@app.route("/call-app2")
def call_app2():
    try:
        res = requests.get("http://app2-service:5000")
        return jsonify({"app1_received": res.json()})
    except Exception as e:
        return jsonify({"error": str(e)})
