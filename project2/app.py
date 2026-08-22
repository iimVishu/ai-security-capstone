from flask import Flask, request, jsonify
import requests

from validate import validate_input, scan_output

app = Flask(__name__)

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "llama3.2:3b"


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({
            "error": "Prompt is required"
        }), 400

    # Layer 1 + Layer 2: Validate user input
    valid, validation_message = validate_input(prompt)

    if not valid:
        return jsonify({
            "error": validation_message
        }), 400

    # Send validated prompt to Ollama
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()
        result = response.json()

        model_response = result.get("response", "")

        # Layer 3: Scan model output
        safe, output_message = scan_output(model_response)

        if not safe:
            return jsonify({
                "error": output_message
            }), 400

        return jsonify({
            "response": model_response
        }), 200

    except requests.exceptions.RequestException as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5001,
        debug=False
    )
