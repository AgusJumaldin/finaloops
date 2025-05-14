import cv2
import numpy as np
import joblib

# Load model components
model = joblib.load("extracted_features/personal_color_model.pkl")
label_encoder = joblib.load("extracted_features/label_encoder.pkl")
scaler = joblib.load("extracted_features/scaler.pkl")

# Load face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def get_average_color(region):
    return np.mean(region.reshape(-1, 3), axis=0)

def get_contrast(gray_img):
    return np.std(gray_img)

def extract_features_from_face(face):
    face = cv2.resize(face, (200, 200))

    skin = face[80:160, 60:140]
    hair = face[0:40, 60:140]
    eye = face[50:80, 80:120]

    skin_ycrcb = cv2.cvtColor(skin, cv2.COLOR_BGR2YCrCb)
    skin_Y, skin_Cr, skin_Cb = get_average_color(skin_ycrcb)
    hair_R, hair_G, hair_B = get_average_color(hair)
    eye_R, eye_G, eye_B = get_average_color(eye)
    contrast = get_contrast(cv2.cvtColor(face, cv2.COLOR_BGR2GRAY))

    return [skin_Y, skin_Cr, skin_Cb, hair_R, hair_G, hair_B, eye_R, eye_G, eye_B, contrast]

# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print(" Failed to open camera.")
    exit()

print(" Press SPACE to capture and predict. Press ESC to exit.")

# Initialize result text
result_text = ""
while True:
    ret, frame = cap.read()
    if not ret:
        print(" Failed to capture frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        if result_text:
            cv2.putText(frame, result_text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.9, (0, 255, 0), 2)

    cv2.imshow("Press SPACE to Predict", frame)
    key = cv2.waitKey(1)

    if key == 27:  # ESC
        break
    elif key == 32:  # SPACE
        if len(faces) == 0:
            print(" No face detected.")
            continue

        x, y, w, h = faces[0]
        face = frame[y:y+h, x:x+w]
        try:
            features = np.array([extract_features_from_face(face)])
            scaled = scaler.transform(features)
            prediction = model.predict(scaled)
            label = label_encoder.inverse_transform(prediction)
            result_text = f"{label[0]}"
            print(f" Predicted Personal Color: {label[0]}")
        except Exception as e:
            result_text = "Prediction failed"
            print(f" Feature extraction failed: {e}")

cap.release()
cv2.destroyAllWindows()