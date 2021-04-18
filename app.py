from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route("/owner")
def owner():
    return f"Hello world from Rick Morrow /{datetime. now()}"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)