from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
from src.detector import predict_emotion

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

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
    app.run(debug=True)
