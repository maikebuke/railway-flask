from flask import Flask, jsonify
import os
import sys
import requests
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": f"Welcome to your Flask app", 
                    "python":  f"{sys.version}",
                    "time": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))})


@app.route("/test")
def test():
    resp = requests.get("https://api.openai.com/v1/chat/completions")
    return resp

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
