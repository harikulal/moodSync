const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const countdownEl = document.getElementById('countdown');
const retakeBtn = document.getElementById('retakeBtn');

navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(err => {
        console.error("Error accessing webcam:", err);
    });

function startCountdown() {
    let count = 3;
    countdownEl.innerText = count;
    const interval = setInterval(() => {
        count--;
        if (count > 0) {
            countdownEl.innerText = count;
        } else {
            clearInterval(interval);
            countdownEl.innerText = '';
            capture();
        }
    }, 1000);
}

function capture() {
    document.querySelector('video').style.display = 'none';
    document.querySelector('.btn').style.display = 'none';
    document.getElementById('loader').style.display = 'block';

    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth || 400;
    canvas.height = video.videoHeight || 300;

    const context = canvas.getContext('2d');
    context.translate(canvas.width, 0);
    context.scale(-1, 1);
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    const imageData = canvas.toDataURL('image/jpeg');

    fetch('/capture', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ image: imageData })
    })
    .then(response => response.text())
    .then(html => {
        document.open();
        document.write(html);
        document.close();
    });
}


function retake() {
    canvas.style.display = 'none';
    retakeBtn.style.display = 'none';
}
