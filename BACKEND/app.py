from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import uuid
from predict import run_prediction

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/predict", methods=["POST"])
def predict_video():
    try:
        file = request.files.get("video")
        if not file:
            return jsonify({"error": "No file received"}), 400

        filename = f"{uuid.uuid4()}.mp4"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        print("📥 File saved:", filepath)

        prediction = run_prediction(filepath)
        print("🤖 Prediction:", prediction)

        # 🔥 MUST return VALID JSON
        return jsonify({"prediction": prediction})

    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
