from flask import Flask, render_template, request, jsonify ,send_from_directory
import cv2
import numpy as np
from src.detector import predict_emotion

app = Flask(__name__, static_folder="static", static_url_path="")

@app.route("/")
def serve_frontend():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"emotion": "No image received"})

    file = request.files["image"]
    npimg = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    if frame is None:
        return jsonify({"emotion": "Invalid frame"})

    emotion = predict_emotion(frame)
    return jsonify({"emotion": emotion})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
