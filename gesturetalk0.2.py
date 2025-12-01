import cv2
import numpy as np
import mediapipe as mp# type: ignore
from tensorflow.keras.models import load_model # type: ignore

# Load model and classes
model = load_model("gesture_model.h5")
classes = np.load("label_classes.npy")

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2)

def extract_hands_only(frame):
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    lh = []
    rh = []

    if results.multi_hand_landmarks:
        for hand, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            label = handedness.classification[0].label  # "Left" or "Right"

            pts = []
            for lm in hand.landmark:
                pts.extend([lm.x, lm.y, lm.z])

            if label == "Left":
                lh = pts
            else:
                rh = pts

    # Fill missing hand with zeros
    if len(lh) == 0: lh = [0] * 63
    if len(rh) == 0: rh = [0] * 63

    return np.array(lh + rh)


def swap_hands(vector_126):
    """Swap left and right hand features."""
    lh = vector_126[:63]
    rh = vector_126[63:]
    return np.array(rh + lh)


# MAIN SCRIPT
video_path = input("Enter video path: ")
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
    print("❌ No frames processed")
    exit()

input_vector = np.mean(all_keypoints, axis=0).reshape(1, -1)

# First try normal prediction
pred1 = model.predict(input_vector)
index1 = np.argmax(pred1)
conf1 = pred1[0][index1]

# If low confidence → try hand swap
if conf1 < 0.70:
    swapped = swap_hands(input_vector[0]).reshape(1, -1)
    pred2 = model.predict(swapped)
    index2 = np.argmax(pred2)
    conf2 = pred2[0][index2]

    if conf2 > conf1:
        print("\n🔄 Hand Swap Used")
        print("🔮 Predicted Action:", classes[index2])
        print("📈 Confidence:", conf2)
        exit()

print("\n🔮 Predicted Action:", classes[index1])
print("📈 Confidence:", conf1)
