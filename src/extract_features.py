import cv2
import os
import numpy as np
import pandas as pd
from tqdm import tqdm

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Base dataset path (adjust if needed)
DATASET_DIR = "Dataset/mst-e_data"
OUTPUT_CSV = "extracted_features/personal_color_features.csv"

# Helper functions
def get_average_color(region):
    return np.mean(region.reshape(-1, 3), axis=0)

def get_contrast(gray_img):
    return np.std(gray_img)

features = []

for tone_label in os.listdir(DATASET_DIR):
    folder_path = os.path.join(DATASET_DIR, tone_label)
    if not os.path.isdir(folder_path):
        continue 

    for img_file in tqdm(os.listdir(folder_path), desc=f"Processing {tone_label}"):
        img_path = os.path.join(folder_path, img_file)

        # Only allow image files
        if not img_file.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue

        img = cv2.imread(img_path)
        if img is None:
            print(f" Could not load image: {img_path}")
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        if len(faces) == 0:
            print(f" No face detected in: {img_path}")
            continue

        x, y, w, h = faces[0]
        face = img[y:y+h, x:x+w]
        face = cv2.resize(face, (200, 200))

        # Extract regions
        skin = face[80:160, 60:140]
        hair = face[0:40, 60:140]
        eye = face[50:80, 80:120]

        skin_ycrcb = cv2.cvtColor(skin, cv2.COLOR_BGR2YCrCb)
        skin_Y, skin_Cr, skin_Cb = get_average_color(skin_ycrcb)
        hair_R, hair_G, hair_B = get_average_color(hair)
        eye_R, eye_G, eye_B = get_average_color(eye)
        contrast = get_contrast(cv2.cvtColor(face, cv2.COLOR_BGR2GRAY))

        features.append([
            skin_Y, skin_Cr, skin_Cb,
            hair_R, hair_G, hair_B,
            eye_R, eye_G, eye_B,
            contrast,
            tone_label  # Label from folder name, e.g., "TONE 1"
        ])

# Save CSV
columns = [
    'skin_Y', 'skin_Cr', 'skin_Cb',
    'hair_R', 'hair_G', 'hair_B',
    'eye_R', 'eye_G', 'eye_B',
    'contrast', 'label'
]

os.makedirs("extracted_features", exist_ok=True)
df = pd.DataFrame(features, columns=columns)
df.to_csv(OUTPUT_CSV, index=False)

print(f"\n Saved {len(df)} records to {OUTPUT_CSV}")
 