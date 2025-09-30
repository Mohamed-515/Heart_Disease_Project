# models/export_model.py

import joblib
import os

MODEL_DIR = "models"
TUNED_MODEL = os.path.join(MODEL_DIR, "svm_tuned.joblib")
FINAL_MODEL = os.path.join(MODEL_DIR, "final_model.pkl")

# Load tuned model
model = joblib.load(TUNED_MODEL)

# Save as final_model.pkl
joblib.dump(model, FINAL_MODEL)
print(" Final model exported to:", FINAL_MODEL)
