from flask import Flask, jsonify, send_file
import pandas as pd
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "auto_parts_inventory.csv")
HTML_FILE = os.path.join(BASE_DIR, "items.html")

@app.route("/inventory")
def get_inventory():
    if not os.path.exists(CSV_FILE):
        return jsonify({"error": "CSV file not found"}), 404
    df = pd.read_csv(CSV_FILE)
    return df.to_json(orient="records")

@app.route("/")
def index():
    return send_file(HTML_FILE)

@app.route("/<path:path>")
def static_files(path):
    return send_file(os.path.join(BASE_DIR, path))

if __name__ == "__main__":
    app.run(debug=True)
