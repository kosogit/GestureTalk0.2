import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential #type: ignore
from tensorflow.keras.layers import Dense, Dropout #type: ignore
from tensorflow.keras.utils import to_categorical #type: ignore

DATA_DIR = "C:/Users/at782/Python/GESTURE_TALK_DATASET"

# Load data
X = []
y = []

for action in os.listdir(DATA_DIR):
    action_path = os.path.join(DATA_DIR, action)
    if os.path.isdir(action_path):
        for file in os.listdir(action_path):
            if file.endswith(".npy"):
                vector = np.load(os.path.join(action_path, file))
                X.append(vector)
                y.append(action)

X = np.array(X)
y = np.array(y)

# Encode labels
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)
y_categorical = to_categorical(y_encoded)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y_categorical, test_size=0.2, random_state=42
)

# Build model
model = Sequential([
    Dense(256, activation='relu', input_shape=(X.shape[1],)),
    Dropout(0.3),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(len(encoder.classes_), activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train
history = model.fit(X_train, y_train, epochs=40, batch_size=16, validation_split=0.1)

# Save model + label encoder
model.save("gesture_model.h5")
np.save("label_classes.npy", encoder.classes_)

print("Training complete! Model saved.")