from flask import Flask, jsonify
import os
import sys

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": f"Welcome to your Flask app, python version: {sys.version}"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
