from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/search")
def search():
    query = request.args.get("q")
    # os.system(f"grep {query} data.txt")  # <- podatność: command injection
    return "Szukam..."
