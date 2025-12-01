import cv2
import numpy as np
import mediapipe as mp
from tensorflow.keras.models import load_model  # type: ignore

# ------------------------------
# LOAD MODEL + LABEL CLASSES
# ------------------------------

model = load_model("gesture_model.h5")
classes = np.load("label_classes.npy")

# Mediapipe Hands
mp_hands = mp.solutions.hands
hands_detector = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# ------------------------------
# EXTRACT HAND KEYPOINTS (126)
# ------------------------------

def extract_keypoints(frame):
    keypoints = []

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands_detector.process(frame_rgb)

    left = None
    right = None

    # Identify LEFT and RIGHT hands properly
    if results.multi_hand_landmarks:
        for hand_lm, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            label = handedness.classification[0].label
            if label == "Left":
                left = hand_lm
            elif label == "Right":
                right = hand_lm

    # ----- LEFT HAND (21 landmarks × 3 = 63) -----
    if left:
        for lm in left.landmark:
            keypoints.extend([lm.x, lm.y, lm.z])
    else:
        keypoints.extend([0] * 63)

    # ----- RIGHT HAND (21 landmarks × 3 = 63) -----
    if right:
        for lm in right.landmark:
            keypoints.extend([lm.x, lm.y, lm.z])
    else:
        keypoints.extend([0] * 63)

    return np.array(keypoints)  # TOTAL = 126


# ------------------------------
#         MAIN CODE
# ------------------------------

video_path = input("Enter video path: ")

cap = cv2.VideoCapture(video_path)

all_keypoints = []

print("\nProcessing video...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    keypoints = extract_keypoints(frame)
    all_keypoints.append(keypoints)

cap.release()

if len(all_keypoints) == 0:
    print("❌ No keypoints extracted! Check video.")
    exit()

# Average over all frames → final input vector (1 × 126)
input_vector = np.mean(all_keypoints, axis=0).reshape(1, -1)

# ------------------------------
#        PREDICT
# ------------------------------

prediction = model.predict(input_vector)
index = np.argmax(prediction)
confidence = prediction[0][index]

print("\n🔮 Predicted Action:", classes[index])
print("📈 Confidence:", round(float(confidence), 3))

if confidence < 0.75:
    print("⚠️ Low confidence. Try a clearer video.")
