from flask import Flask, request, jsonify
from flask_cors import CORS
from ai import response

app = Flask(__name__)
CORS(app)

@app.route("/response", methods=["POST"])
def code():
    data = request.get_json()
    if not data or "code" not in data:
        return jsonify({"error": "Please provide code in JSON format"}), 400

    code_input = data.get("code")
    language = data.get("language")

    try:
        ai_response = response(code_input, language)
        return jsonify(ai_response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
