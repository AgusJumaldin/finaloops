import joblib
import numpy as np
import os

# Load saved model, encoder, and scaler
model_path = "extracted_features/personal_color_model.pkl"
encoder_path = "extracted_features/label_encoder.pkl"
scaler_path = "extracted_features/scaler.pkl"

# Check if required files exist
for path in [model_path, encoder_path, scaler_path]:
    if not os.path.exists(path):
        print(f" Missing: {path}. Make sure you ran the training script first.")
        exit()

# Load model and helpers
model = joblib.load(model_path)
label_encoder = joblib.load(encoder_path)
scaler = joblib.load(scaler_path)

# Sample input for prediction
# Format: [skin_Y, skin_Cr, skin_Cb, hair_R, hair_G, hair_B, eye_R, eye_G, eye_B, contrast]
# Replace with real values if you have them
sample_input = np.array([
    [170, 145, 120, 80, 60, 50, 40, 50, 60, 0.82]
])

# Normalize input
scaled_input = scaler.transform(sample_input)

# Predict label
predicted_class_index = model.predict(scaled_input)
predicted_label = label_encoder.inverse_transform(predicted_class_index)

# Output result
print(" Predicted Personal Color Type:", predicted_label[0])
