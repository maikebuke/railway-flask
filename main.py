from flask import Flask, jsonify
import os
import sys
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": f"Welcome to your Flask app, python version: {sys.version}",
                    "time": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
