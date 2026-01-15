const video = document.getElementById("video");
const emotionText = document.getElementById("emotion");

window.onload = () => {
  navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
      video.srcObject = stream;
      video.play();
    })
    .catch(err => {
      console.error(err);
      emotionText.innerText = "Camera access denied";
    });

  setInterval(() => {
    if (video.videoWidth === 0) return;

    const canvas = document.createElement("canvas");
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    const ctx = canvas.getContext("2d");
    ctx.drawImage(video, 0, 0);

    canvas.toBlob(blob => {
      const formData = new FormData();
      formData.append("image", blob);

      fetch("/predict", { method: "POST", body: formData })
        .then(res => res.json())
        .then(data => {
          emotionText.innerText = "Emotion: " + data.emotion;
        });
    }, "image/jpeg");
  }, 1000);
};
