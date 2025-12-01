# 📘 GestureTalk AI – Sign Language to Speech Converter

# 

# GestureTalk AI is an intelligent real-time sign language recognition system built to improve communication between the deaf community and the hearing population. Using MediaPipe, TensorFlow, scikit-learn, and OpenCV, the system detects hand gestures via webcam and converts them instantly into text and speech.

# 

# 🚀 Features

# 

# ✋ Real-time gesture tracking using MediaPipe Hand Landmark Detection

# 

# 🧠 Custom-trained ML model for accurate sign classification

# 

# 🎤 Text-to-Speech output for smooth communication

# 

# 🎯 Supports multiple gestures with high accuracy

# 

# 🪶 Lightweight, fast, and optimized for real-time performance

# 

# 🧩 Easy to extend with new gestures and models

# 

# 🛠️ Tech Stack

# 

# Languages: Python

# Libraries:

# 

# MediaPipe

# 

# TensorFlow

# 

# scikit-learn

# 

# NumPy

# 

# OpenCV

# 

# pyttsx3 (for speech output)

# 

# 📁 Project Structure

# GestureTalk-AI/

# │── data/               # Dataset for gesture training

# │── model/              # Saved ML model files

# │── src/                # Main program code

# │   ├── collect\_data.py

# │   ├── train\_model.py

# │   ├── recognize.py

# │── README.md

# │── requirements.txt

# 

# ⚙️ How It Works

# 

# MediaPipe detects hand landmarks (21 coordinates per hand).

# 

# Coordinates are converted into a numerical dataset.

# 

# A TensorFlow model is trained to classify gestures.

# 

# In real time, the model predicts the gesture shown to the camera.

# 

# The system displays the prediction and optionally speaks it aloud.
######How to RUN :-################################################
run this code to terminal 
   pip install -r requirements.txt
then use trainer.py create the data set 
then create the model using createModel.py



