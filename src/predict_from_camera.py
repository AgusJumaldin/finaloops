import cv2
import numpy as np
import joblib
import os

# === Load model and tools ===
model_path = "extracted_features/personal_color_model.pkl"
encoder_path = "extracted_features/label_encoder.pkl"
scaler_path = "extracted_features/scaler.pkl"

for path in [model_path, encoder_path, scaler_path]:
    if not os.path.exists(path):
        print(f" Missing: {path}. Please train the model first.")
        exit()

model = joblib.load(model_path)
label_encoder = joblib.load(encoder_path)
scaler = joblib.load(scaler_path)

# === Haar cascade face detector ===
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
if face_cascade.empty():
    print(" Could not load Haar cascade.")
    exit()

# === Helper functions ===
def get_average_color(region):
    return np.mean(region.reshape(-1, 3), axis=0)

def get_contrast(gray_img):
    return np.std(gray_img)

def extract_features(face_img):
    face = cv2.resize(face_img, (200, 200))
    skin = face[80:160, 60:140]
    hair = face[0:40, 60:140]
    eye = face[50:80, 80:120]

    skin_ycrcb = cv2.cvtColor(skin, cv2.COLOR_BGR2YCrCb)
    skin_Y, skin_Cr, skin_Cb = get_average_color(skin_ycrcb)
    hair_R, hair_G, hair_B = get_average_color(hair)
    eye_R, eye_G, eye_B = get_average_color(eye)
    contrast = get_contrast(cv2.cvtColor(face, cv2.COLOR_BGR2GRAY))

    return [skin_Y, skin_Cr, skin_Cb, hair_R, hair_G, hair_B, eye_R, eye_G, eye_B, contrast]

# === Start webcam ===
cap = cv2.VideoCapture(0)
cv2.namedWindow("Personal Color Detection", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Personal Color Detection", 1280, 760)
if not cap.isOpened():
    print(" Failed to open webcam.")
    exit()

print(" Camera started. Press SPACE to predict, ESC to quit.")
predicted_label_text = ""

while True:
    ret, frame = cap.read()
    if not ret:
        print(" Failed to read frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        # Draw face box
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Show predicted label if available
        if predicted_label_text:
            cv2.putText(frame, f"Predicted: {predicted_label_text}",
                        (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.9, (0, 255, 0), 2, cv2.LINE_AA)

    # Show window
    cv2.imshow("Personal Color Detection", frame)

    key = cv2.waitKey(1)
    if key == 27:  # ESC
        break
    elif key == 32 and len(faces) > 0:  # SPACE
        x, y, w, h = faces[0]
        face_img = frame[y:y+h, x:x+w]

        try:
            features = np.array([extract_features(face_img)])
            scaled = scaler.transform(features)
            prediction = model.predict(scaled)
            predicted_label_text = label_encoder.inverse_transform(prediction)[0]
            print(f" Predicted Skin Tone: {predicted_label_text}")
        except Exception as e:
            print(f" Prediction failed: {e}")
            predicted_label_text = ""

cap.release()
cv2.destroyAllWindows()
