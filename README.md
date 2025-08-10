# 🎵 moodSync — AI-Powered Emotion-Based Music Player

> Let your face set the vibe!  
> A web application that detects your mood through your webcam and plays music that matches your emotions — all in real time.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Backend-lightgrey)
![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-red)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

📌 Overview

moodSync captures your facial expression via webcam, detects your emotion using a deep learning model, and plays a song that matches your mood.

---

 ✨ Features

- 📸 Live Emotion Detection** — Uses OpenCV to detect faces in real time.
- 🧠 AI-Powered Classification** — Pretrained deep learning model (`emotion_model.h5`) classifies emotions like:
  - Angry 😠
  - Disgust 🤢
  - Fear 😨
  - Happy 😄
  - Neutral 😐
  - Sad 😢
  - Surprise 😲
- 🎶 Mood-Based Music Playback** — Pygame plays MP3 files that match your detected emotion.
- 💻 Simple Web Interface** — Flask backend with HTML/CSS templates for an intuitive user experience.

---

 🛠 Tech Stack

| Component          | Technology Used           |
|--------------------|---------------------------|
| Backend            | Flask (Python)            |
| Frontend           | HTML, CSS, Jinja Templates|
| AI Model           | Keras, TensorFlow         |
| Vision             | OpenCV                    |
| Audio              | Pygame                    |

