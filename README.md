📘 GestureTalk AI

<<<<<<< HEAD
##

## GestureTalk AI is an intelligent real-time sign language recognition system built to improve communication between the deaf community and the hearing population. Using MediaPipe, TensorFlow, scikit-learn, and OpenCV, the system detects hand gestures via webcam and converts them instantly into text and speech.

##
=======
GestureTalk AI is a simple tool that recognizes hand gestures using AI. It uses a webcam to detect signs and converts them into text and speech. The goal is to help improve communication for people with hearing impairments.

🚀 Features

Real-time hand tracking
>>>>>>> a2a6c9a339a346dbcd9ad471fb55f0eda8cdc99c

Fast and accurate gesture recognition

<<<<<<< HEAD
##

## ✋ Real-time gesture tracking using MediaPipe Hand Landmark Detection

## 

## 🧠 Custom-trained ML model for accurate sign classification

## 

## 🎤 Text-to-Speech output for smooth communication

## 

## 🎯 Supports multiple gestures with high accuracy

## 

## 🪶 Lightweight, fast, and optimized for real-time performance

## 

## 🧩 Easy to extend with new gestures and models

## 
=======
Converts signs to text

Optional speech output

Easy to train and add new gestures

🛠️ Technologies Used

Python

MediaPipe

TensorFlow

OpenCV

NumPy

scikit-learn



🚀 How to Run the Project
✅ Step 1: Install Dependencies
>>>>>>> a2a6c9a339a346dbcd9ad471fb55f0eda8cdc99c

Run this command in your terminal:

<<<<<<< HEAD
## 

## Languages: Python

## Libraries:

## 

## MediaPipe

## 

## TensorFlow

## 

## scikit-learn

## 

## NumPy

##

## OpenCV

## 

## pyttsx3 (for speech output)

## 

# 📁 Project Structure

## GestureTalk-AI/

## │── data/               # Dataset for gesture training

## │── model/              # Saved ML model files

## │── src/                # Main program code

## │   ├── collect\_data.py

## │   ├── train\_model.py

## │   ├── recognize.py

## │── README.md

## │── requirements.txt

## 

# ⚙️ How It Works

### 

## MediaPipe detects hand landmarks (21 coordinates per hand).

###

## Coordinates are converted into a numerical dataset.

### 

## A TensorFlow model is trained to classify gestures.

### 

## In real time, the model predicts the gesture shown to the camera.

### 

## The system displays the prediction and optionally speaks it aloud.
# 🚀 How to Run the Project
## ✅ Step 1: Install Dependencies
=======
pip install -r requirements.txt

✅ Step 2: Create the Dataset

Use the trainer script to collect gesture data:

python trainer.py

✅ Step 3: Train & Generate the Model

After collecting data, train your model:

python createModel.py


>>>>>>> a2a6c9a339a346dbcd9ad471fb55f0eda8cdc99c

### Run this command in your terminal:

- `pip install -r requirements.txt`

## ✅ Step 2: Create the Dataset

### Use the trainer script to collect gesture data:

- `python trainer.py`

## ✅ Step 3: Train & Generate the Model

### After collecting data, train your model:

- `python createModel.py`
