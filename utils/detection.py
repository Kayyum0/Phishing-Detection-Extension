import os
import pickle
import re
from urllib.parse import urlparse
import numpy as np
import pandas as pd  # Import pandas
from utils.feature import FeatureExtraction  # Ensure relative import is correct

# Define the path to the trained model.
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'model', 'model.pkl')

# Load the trained model once when the module is imported.
try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    print("Error loading model:", e)
    model = None

def predict_phishing(url):
    """
    Predicts whether the given URL is phishing.
    Returns a dictionary with:
      - isPhishing: Boolean result.
      - confidence: Model's confidence (if available).
      - features: The feature vector used for prediction.
      - message: A human-readable summary.
    """
    if model is None:
        raise Exception("Model not loaded. Cannot perform prediction.")

    # Use your FeatureExtraction class to extract features.
    obj = FeatureExtraction(url)
    features = obj.getFeaturesList()

    # Verify the feature vector length (should be 30)
    if len(features) != 30:
        raise ValueError(f"Extracted {len(features)} features; expected 30 features.")

    # Create a numpy array with the correct shape (1, 30)
    x = np.array(features).reshape(1, 30)
    
    # Define the feature names that the model was trained on.
    feature_names = [
        "UsingIP", "LongURL", "ShortURL", "Symbol@", "Redirecting//",
        "PrefixSuffix-", "SubDomains", "HTTPS", "DomainRegLen", "Favicon",
        "NonStdPort", "HTTPSDomainURL", "RequestURL", "AnchorURL", "LinksInScriptTags",
        "ServerFormHandler", "InfoEmail", "AbnormalURL", "WebsiteForwarding", "StatusBarCust",
        "DisableRightClick", "UsingPopupWindow", "IframeRedirection", "AgeofDomain",
        "DNSRecording", "WebsiteTraffic", "PageRank", "GoogleIndex", "LinksPointingToPage",
        "StatsReport"
    ]

    # Convert the array to a DataFrame with proper feature names
    df_features = pd.DataFrame(x, columns=feature_names)

    # Predict using the model
    try:
        prediction = model.predict(df_features)
    except Exception as e:
        print("Error during model prediction:", e)
        raise e
    
    # Interpret the prediction (modify this logic according to your model's training)
    # Example: if prediction 1 means safe and -1 means phishing
    if prediction[0] == 1:
        is_phishing = False  # 1 means safe
    elif prediction[0] == -1:
        is_phishing = True   # -1 means unsafe (phishing)
    else:
        raise ValueError(f"Unexpected prediction value: {prediction[0]}")
    
    # Determine confidence if available
    confidence = None
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(df_features)
        try:
            phishing_index = list(model.classes_).index(1)
        except ValueError:
            phishing_index = 0
        confidence = proba[0][phishing_index]
    else:
        confidence = 1.0 if prediction[0] == 1 else 0.0
    
    message = "The URL appears to be malicious." if is_phishing else "The URL appears to be safe."
    if confidence is not None:
        message += f" (Confidence: {confidence:.2f})"
    
    return {
        'isPhishing': is_phishing,
        'confidence': confidence,
        'features': features,
        'message': message
    }
