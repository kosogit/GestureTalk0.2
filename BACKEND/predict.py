import cv2
import numpy as np
import mediapipe as mp
from tensorflow.keras.models import load_model# type: ignore

# -----------------------------------
# Load Model + Label Classes
# -----------------------------------
model = load_model("gesture_model.h5")
classes = np.load("label_classes.npy")

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2)


# -----------------------------------
# Extract 126 keypoints (Left + Right hand)
# -----------------------------------
def extract_hands_only(frame):
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    lh, rh = [], []

    if results.multi_hand_landmarks:
        for hand, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            label = handedness.classification[0].label
            pts = []

            for lm in hand.landmark:
                pts.extend([lm.x, lm.y, lm.z])

            if label == "Left":
                lh = pts
            elif label == "Right":
                rh = pts

    if len(lh) == 0: lh = [0] * 63
    if len(rh) == 0: rh = [0] * 63

    return np.array(lh + rh)


# -----------------------------------
# Swap hands (in case user flips hands)
# -----------------------------------
def swap_hands(vec):
    lh = vec[:63]
    rh = vec[63:]
    return np.array(rh + lh)


# -----------------------------------
# Main Prediction Function (Flask calls this)
# -----------------------------------
def run_prediction(video_path):
    cap = cv2.VideoCapture(video_path)
    all_keypoints = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        keypoints = extract_hands_only(frame)
        all_keypoints.append(keypoints)

    cap.release()

    if len(all_keypoints) == 0:
        return "No keypoints found"

    input_vec = np.mean(all_keypoints, axis=0).reshape(1, -1)

    # Normal prediction
    pred1 = model.predict(input_vec)
    idx1 = np.argmax(pred1)
    conf1 = pred1[0][idx1]

    # Try swapped hands if confidence is low
    if conf1 < 0.70:
        swapped = swap_hands(input_vec[0]).reshape(1, -1)
        pred2 = model.predict(swapped)
        idx2 = np.argmax(pred2)
        conf2 = pred2[0][idx2]

        if conf2 > conf1:
            return f"{classes[idx2]} (hand-swapped)"

    return f"{classes[idx1]}"
