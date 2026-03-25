from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import traceback
from threat_analyzer import analyze

app = Flask(__name__, static_folder="static", static_url_path="/static")
CORS(app)


@app.route("/")
def index():
    return send_from_directory("static", "home.html")


@app.route("/app")
def analyzer():
    return send_from_directory("static", "index.html")


@app.route("/analyze", methods=["POST"])
def analyze_threat():
    try:
        data = request.get_json()
        if not data or "input" not in data:
            return jsonify({"error": "Missing 'input' field in request body"}), 400

        user_input = data["input"]
        result = analyze(user_input)
        return jsonify(result)

    except ValueError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": f"Analysis failed: {str(e)}"}), 500


if __name__ == "__main__":
    print("=" * 60)
    print("  ThreatGPT — AI Cybersecurity Analyst")
    # print("  Running at: http://127.0.0.1:5000")
    print("=" * 60)
    # app.run(debug=True, host="127.0.0.1", port=5000)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
