# 📘 GestureTalk AI


##

## GestureTalk AI is an intelligent real-time sign language recognition system built to improve communication between the deaf community and the hearing population. Using MediaPipe, TensorFlow, scikit-learn, and OpenCV, the system detects hand gestures via webcam and converts them instantly into text and speech.

##



# 🚀 Features

## Real-time hand tracking

## Fast and accurate gesture recognition

## ✋ Real-time gesture tracking using MediaPipe Hand Landmark Detection

## 🧠 Custom-trained ML model for accurate sign classification

## 🎤 Text-to-Speech output for smooth communication

## 🎯 Supports multiple gestures with high accuracy

## 🪶 Lightweight, fast, and optimized for real-time performance

## 🧩 Easy to extend with new gestures and models
#
# 🛠️ Technologies Used

## Python
## MediaPipe
## TensorFlow
## OpenCV
## NumPy
## scikit-learn
#
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

#
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

#
# 🚀 How to Run the Project
## ✅ Step 1: Install Dependencies
### Run this command in your terminal:
- `pip install -r requirements.txt`
## ✅ Step 2: Create the Dataset
### Use the trainer script to collect gesture data:
- `python trainer.py`
## ✅ Step 3: Train & Generate the Model
### After collecting data, train your model:
- `python createModel.py`
