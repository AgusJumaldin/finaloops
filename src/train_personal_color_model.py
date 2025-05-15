import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

# Load the feature dataset
csv_path = "extracted_features/personal_color_features.csv"

if not os.path.exists(csv_path):
    print(" CSV file not found. Run extract_features.py first.")
    exit()

df = pd.read_csv(csv_path)

# Split features and labels
X = df.drop("label", axis=1)
y = df["label"]

# Encode labels (e.g., Light_Spring → 0)
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)

# Train classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(" Model trained with accuracy:", round(acc * 100, 2), "%")
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

# Save model and tools
output_dir = "extracted_features"
os.makedirs(output_dir, exist_ok=True)
joblib.dump(model, os.path.join(output_dir, "personal_color_model.pkl"))
joblib.dump(label_encoder, os.path.join(output_dir, "label_encoder.pkl"))
joblib.dump(scaler, os.path.join(output_dir, "scaler.pkl"))

print(f"\n Model and preprocessing tools saved in '{output_dir}/'")
