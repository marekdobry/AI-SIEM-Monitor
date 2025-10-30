from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import numpy as np

# Expanded training alerts
training_alerts = [
    "Multiple failed SSH login attempts from same IP",
    "File integrity check failed on system32",
    "User login successful",
    "Low disk space warning",
    "Malware detected in quarantine folder",
    "Suspicious process running as root",
    "New user added to admin group",
    "Package installation failed",
    "Firewall configuration changed",
    "Successful sudo to ROOT executed"
]

# Labels (1 = HIGH, 0 = LOW)
labels = [1, 1, 0, 0, 1, 1, 1, 1, 1, 1]

# Create a TF-IDF + Logistic Regression pipeline with n-grams
model = make_pipeline(
    TfidfVectorizer(ngram_range=(1,2), stop_words='english'),
    LogisticRegression(max_iter=500)
)

# Train the model
model.fit(training_alerts, labels)

def classify_alert(alert_text):
    """
    Classifies alert text as HIGH or LOW severity using the trained model.
    """
    prob = model.predict_proba([alert_text])[0][1]  # Probability of HIGH
    if prob > 0.5:
        return "HIGH"
    else:
        return "LOW"
