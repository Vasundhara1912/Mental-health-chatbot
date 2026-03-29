import random

# Each emotion maps to:
#   - responses: empathetic messages the bot will say
#   - tips: relaxation / coping tips to suggest

EMOTION_RESPONSES = {
    "happy": {
        "responses": [
            "That's wonderful to hear! Your positive energy is truly uplifting. 😊",
            "It's great that you're feeling good! Cherish this moment — you deserve it.",
            "Happiness looks good on you! Keep embracing these positive feelings.",
        ],
        "tips": [
            "Keep the good energy going — write down 3 things you're grateful for today.",
            "Share your joy with someone you care about. Positivity is contagious!",
            "Take a moment to savour this feeling. A short walk in fresh air can extend it.",
        ],
        "emoji": "😊",
        "color": "#22c55e"
    },
    "sad": {
        "responses": [
            "I'm really sorry you're feeling this way. It's okay to feel sad — your emotions are valid. 💙",
            "It sounds like you're going through a tough time. I'm here for you, and things will get better.",
            "Feeling sad is a natural part of life. You're not alone — please be gentle with yourself.",
        ],
        "tips": [
            "Try the 5-4-3-2-1 grounding technique: name 5 things you see, 4 you can touch, 3 you hear, 2 you smell, 1 you taste.",
            "Write your feelings in a journal — putting emotions into words can lighten the weight.",
            "Reach out to a trusted friend or family member. Talking helps more than you think.",
            "A warm shower or cup of tea can bring small comfort. Take care of your body too.",
        ],
        "emoji": "💙",
        "color": "#3b82f6"
    },
    "anxious": {
        "responses": [
            "I can sense you're feeling anxious. Take a slow, deep breath — you are safe right now. 🌿",
            "Anxiety can feel overwhelming, but you've handled difficult moments before and you can do this too.",
            "It's okay to feel nervous. Let's slow things down — one step, one breath at a time.",
        ],
        "tips": [
            "Try box breathing: inhale for 4 seconds, hold for 4, exhale for 4, hold for 4. Repeat 4 times.",
            "Write down your worry, then write one realistic best-case outcome next to it.",
            "Ground yourself: place both feet flat on the floor and notice the sensation — you are here, you are safe.",
            "Limit caffeine for now. Even a short 10-minute walk reduces anxiety hormones significantly.",
        ],
        "emoji": "🌿",
        "color": "#f59e0b"
    },
    "angry": {
        "responses": [
            "It sounds like something really frustrated you. Your feelings are completely valid. 🔥",
            "I hear you — anger is a signal that something feels unfair or hurtful. Let's work through it.",
            "It's okay to feel angry. What matters is how we channel it. I'm here to listen.",
        ],
        "tips": [
            "Before reacting, count slowly to 10. This simple pause can prevent regret.",
            "Try progressive muscle relaxation: clench your fists tight for 5 seconds, then slowly release.",
            "Step outside for a few minutes. Physical movement helps discharge anger energy from the body.",
            "Write an unsent letter expressing everything you feel — then tear it up or delete it.",
        ],
        "emoji": "🔥",
        "color": "#ef4444"
    },
    "neutral": {
        "responses": [
            "Thanks for sharing. I'm here whenever you need to talk. 🙂",
            "It sounds like a regular day. Sometimes steady is just right — how can I support you?",
            "I'm listening. Feel free to share anything that's on your mind.",
        ],
        "tips": [
            "Even on calm days, a 5-minute mindfulness check-in can boost your mental clarity.",
            "Is there something small you could do today that would make tomorrow a little easier?",
            "Stay hydrated and take regular screen breaks — small habits, big impact.",
        ],
        "emoji": "🙂",
        "color": "#8b5cf6"
    }
}


def get_response(emotion: str) -> dict:
    """
    Given a detected emotion string, return a random empathetic response + tip.
    Returns a dict with keys: emotion, emoji, color, message, tip
    """
    emotion = emotion.lower().strip()
    if emotion not in EMOTION_RESPONSES:
        emotion = "neutral"

    data = EMOTION_RESPONSES[emotion]
    return {
        "emotion": emotion,
        "emoji": data["emoji"],
        "color": data["color"],
        "message": random.choice(data["responses"]),
        "tip": random.choice(data["tips"]),
    }
