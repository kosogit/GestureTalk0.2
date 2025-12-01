import os
import cv2
import numpy as np
import mediapipe as mp # type: ignore


# Mediapipe Hands Model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

def extract_hand_keypoints(results):
    keypoints = []

    # LEFT HAND
    if results.multi_hand_landmarks:
        left = None
        right = None

        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            label = handedness.classification[0].label
            if label == 'Left':
                left = hand_landmarks
            elif label == 'Right':
                right = hand_landmarks

        # Left hand (21 x,y,z)
        if left:
            for lm in left.landmark:
                keypoints.extend([lm.x, lm.y, lm.z])
        else:
            keypoints.extend([0] * 63)

        # Right hand (21 x,y,z)
        if right:
            for lm in right.landmark:
                keypoints.extend([lm.x, lm.y, lm.z])
        else:
            keypoints.extend([0] * 63)

    else:
        keypoints = [0] * 126  # No hands detected

    return np.array(keypoints)

# ==============================
# MAIN DATA COLLECTION LOOP
# ==============================
dataset_path = "C:/Users/at782/Python/GESTURE_TALK_DATASET"

while True:
    action = input("Enter action name (or type EXIT): ")

    if action.upper() == "EXIT":
        break

    # Convert to UPPERCASE
    action_name = action.upper()

    # Create folder if not exists
    action_folder = os.path.join(dataset_path, action_name)
    os.makedirs(action_folder, exist_ok=True)

    video_path = input(f"Enter video path for {action_name}: ")

    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    print(f"\nExtracting keypoints for {action_name}...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        # Extract 42 keypoints
        keypoints = extract_hand_keypoints(results)

        # Save keypoints
        save_path = os.path.join(action_folder, f"{action_name}_{frame_count}.npy")
        np.save(save_path, keypoints)
        frame_count += 1

    cap.release()
    print(f"Saved {frame_count} frames for {action_name}\n")
