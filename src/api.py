from flask import Flask, request, jsonify
from emma.emma_core import run_emma

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Emma API is running"

@app.route("/run", methods=["POST"])
def run():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No input provided"}), 400

    run_emma(data)

    return jsonify({
        "status": "success",
        "message": "Emma executed successfully"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)