from flask import Flask, request, jsonify
from ai import response  # your AI function

app = Flask(__name__)

@app.route("/", methods=["POST"])
def code():
    data = request.get_json()
    if not data or "code" not in data:
        return jsonify({"error": "Please provide code in JSON format"}), 400

    code_input = data.get("code")
    responses = response(code_input)  # call your AI logic
    return jsonify({"response": responses})

if __name__ == "__main__":
    app.run(debug=True)
