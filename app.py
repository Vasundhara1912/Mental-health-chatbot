from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import re
import os
import nltk
from nltk.corpus import stopwords
from responses import get_response

# ---------- Setup ----------
app = Flask(__name__)
CORS(app)  # Allow requests from the React frontend

nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))

# ---------- Load Model ----------
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model', 'sentiment_model.pkl')

model = None
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
    print(f"Model loaded from {MODEL_PATH}")
else:
    print("WARNING: Model file not found. Train the model first using the Jupyter notebook.")


# ---------- Text Cleaning (must match training preprocessing) ----------
def clean_text(text: str) -> str:
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    tokens = [w for w in text.split() if w not in stop_words]
    return ' '.join(tokens)


# ---------- Routes ----------

@app.route('/health', methods=['GET'])
def health():
    """Simple health check endpoint."""
    return jsonify({
        "status": "ok",
        "model_loaded": model is not None
    })


@app.route('/chat', methods=['POST'])
def chat():
    """
    Main chat endpoint.
    Expects JSON body: { "message": "I feel so stressed today" }
    Returns JSON:  { "emotion": "anxious", "emoji": "🌿", "color": "#f59e0b",
                     "message": "...", "tip": "..." }
    """
    data = request.get_json()

    # Validate input
    if not data or 'message' not in data:
        return jsonify({"error": "Missing 'message' field in request body."}), 400

    user_message = data['message'].strip()
    if not user_message:
        return jsonify({"error": "Message cannot be empty."}), 400

    # Predict emotion
    if model is not None:
        cleaned = clean_text(user_message)
        emotion = model.predict([cleaned])[0]
    else:
        # Fallback if model not yet trained — basic keyword matching
        emotion = fallback_predict(user_message)

    # Build empathetic response
    response = get_response(emotion)
    return jsonify(response)


def fallback_predict(text: str) -> str:
    """Simple keyword-based fallback when ML model is not available."""
    text = text.lower()
    if any(w in text for w in ['happy', 'great', 'wonderful', 'excited', 'love', 'amazing']):
        return 'happy'
    if any(w in text for w in ['sad', 'lonely', 'cry', 'depressed', 'hopeless', 'miserable']):
        return 'sad'
    if any(w in text for w in ['anxious', 'worried', 'stress', 'nervous', 'panic', 'fear', 'scared']):
        return 'anxious'
    if any(w in text for w in ['angry', 'furious', 'mad', 'frustrated', 'hate', 'irritated']):
        return 'angry'
    return 'neutral'


# ---------- Run ----------
if __name__ == '__main__':
    app.run(debug=True, port=5000)
