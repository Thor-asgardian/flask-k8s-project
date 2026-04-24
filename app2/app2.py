from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"app": "app2", "message": "Hello from App2"})
