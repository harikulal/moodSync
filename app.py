from flask import Flask, render_template, request
import cv2
import numpy as np
import base64
import re
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import pygame
import random
import os

app = Flask(__name__)

# Load emotion model and face detector
model = load_model("emotion_model.h5")
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

# Two songs per emotion
music_map = {
    'angry': ['static/music/angry1.mp3', 'static/music/angry2.mp3'],
    'disgust': ['static/music/disgust1.mp3', 'static/music/disgust2.mp3'],
    'fear': ['static/music/fear1.mp3', 'static/music/fear2.mp3'],
    'happy': ['static/music/happy1.mp3', 'static/music/happy2.mp3'],
    'neutral': ['static/music/neutral1.mp3', 'static/music/neutral2.mp3'],
    'sad': ['static/music/sad1.mp3', 'static/music/sad2.mp3'],
    'surprise': ['static/music/surprise1.mp3', 'static/music/surprise2.mp3']
}

pygame.mixer.init()

def stop_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()

@app.route('/')
def index():
    stop_music()
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/capture_page')
def capture_page():
    return render_template('capture.html')

@app.route('/capture', methods=['POST'])
def capture():
    stop_music()
    data = request.get_json()
    if not data or 'image' not in data:
        return "Invalid image data", 400

    image_data = re.sub('^data:image/.+;base64,', '', data['image'])
    image_bytes = base64.b64decode(image_data)
    np_arr = np.frombuffer(image_bytes, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    if frame is None:
        return "Image decode failed", 500

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    emotion = "No face detected"
    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        roi = gray[y:y+h, x:x+w]
        roi = cv2.resize(roi, (48, 48))
        roi = roi.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)

        preds = model.predict(roi, verbose=0)[0]

        if len(preds) == len(emotion_labels):
            emotion = emotion_labels[np.argmax(preds)]
            if emotion in music_map:
                song = random.choice(music_map[emotion])
                pygame.mixer.music.load(song)
                pygame.mixer.music.play()
        else:
            emotion = "Unknown"

    image_path = os.path.join("static", "capture.jpg")
    cv2.imwrite(image_path, frame)


    return render_template('result.html', emotion=emotion, image='capture.jpg')

if __name__ == '__main__':
    app.run(debug=True)
