# Mental Health Companion Chatbot

A full-stack AI chatbot that detects student mood through sentiment analysis and responds with empathy, motivation, and relaxation tips.

---

## Project Structure

```
mental-health-chatbot/
├── notebook/
│   └── train_model.ipynb       ← Train the ML model here
├── backend/
│   ├── app.py                  ← Flask API
│   ├── responses.py            ← Emotion → response mapping
│   ├── requirements.txt
│   └── model/                  ← Saved model goes here after training
└── frontend/
    ├── src/
    │   ├── App.jsx
    │   ├── App.css
    │   ├── ChatWindow.jsx
    │   ├── MoodBadge.jsx
    │   └── main.jsx
    ├── index.html
    ├── package.json
    └── vite.config.js
```

---

## Step 1 — Train the Model

### Download the GoEmotions dataset
1. Go to: https://github.com/google-research/google-research/tree/master/goemotions/data
2. Download `train.tsv`, `dev.tsv`, `test.tsv`
3. Place them inside the `notebook/` folder

### Run the notebook
```bash
cd notebook
jupyter notebook train_model.ipynb
```
Run all cells. The trained model will be saved to `backend/model/sentiment_model.pkl`.

> **Note:** If you don't have the dataset yet, the notebook includes a small demo dataset so you can test the full pipeline right away.

---

## Step 2 — Run the Backend

```bash
cd backend

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the Flask server
python app.py
```

The backend runs on **http://localhost:5000**

**Test it works:**
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "I feel so anxious about my exams"}'
```

---

## Step 3 — Run the Frontend

```bash
cd frontend

# Install packages
npm install

# Start the dev server
npm run dev
```

Open **http://localhost:3000** in your browser.

---

## How It Works

```
User types message
       ↓
React sends POST /chat to Flask
       ↓
Flask cleans text (lowercase, remove noise)
       ↓
ML Model predicts emotion (happy/sad/anxious/angry/neutral)
       ↓
responses.py picks empathetic message + relaxation tip
       ↓
JSON response sent back to React
       ↓
ChatWindow renders mood badge + tip card
```

---

## Emotions Detected

| Emotion  | Emoji | Example input |
|----------|-------|---------------|
| Happy    | 😊    | "I feel great today!" |
| Sad      | 💙    | "I feel lonely and hopeless" |
| Anxious  | 🌿    | "I'm so stressed about exams" |
| Angry    | 🔥    | "I'm really frustrated" |
| Neutral  | 🙂    | "Just a regular day" |

---

## Upgrading the Model (Optional)

To improve accuracy, swap TF-IDF + Logistic Regression for DistilBERT:

```bash
pip install transformers torch datasets
```

Then in the notebook, replace the pipeline with:
```python
from transformers import pipeline
classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")
```

---

## Deployment

**Backend → Render.com (free tier)**
1. Push `backend/` to a GitHub repo
2. Create a new Web Service on render.com
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`

**Frontend → Vercel (free tier)**
1. Push `frontend/` to a GitHub repo
2. Import the repo on vercel.com
3. Vercel auto-detects Vite and deploys

---

## Important Disclaimer

This chatbot is an academic project and **not** a substitute for professional mental health care. Always include crisis helpline information in production apps.
