import joblib
import numpy as np

# Load model, encoder, and scaler
model = joblib.load("personal_color_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")
scaler = joblib.load("scaler.pkl")

# Example new input: [skin_Y, skin_Cr, skin_Cb, hair_R, hair_G, hair_B, eye_R, eye_G, eye_B, contrast]
new_data = np.array([[170, 145, 120, 80, 60, 50, 40, 50, 60, 0.8]])
scaled = scaler.transform(new_data)
prediction = model.predict(scaled)
label = label_encoder.inverse_transform(prediction)

print("Predicted Personal Color:", label[0])
