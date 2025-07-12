from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Load the GoEmotions model and tokenizer
model_name = "SamLowe/roberta-base-go_emotions"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Create a pipeline
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer, top_k=1)

# (Optional) Clean label mapping to match your coping prompt labels
label_map = {
    "admiration": "admiration",
    "amusement": "amusement",
    "anger": "anger",
    "annoyance": "annoyance",
    "approval": "approval",
    "caring": "caring",
    "confusion": "confusion",
    "curiosity": "curiosity",
    "desire": "desire",
    "disappointment": "disappointment",
    "disapproval": "disapproval",
    "disgust": "disgust",
    "embarrassment": "embarrassment",
    "excitement": "excitement",
    "fear": "fear",
    "gratitude": "gratitude",
    "grief": "grief",
    "joy": "joy",
    "love": "love",
    "nervousness": "nervousness",
    "optimism": "optimism",
    "pride": "pride",
    "realization": "realization",
    "relief": "relief",
    "remorse": "guilt",
    "sadness": "sadness",
    "surprise": "surprise",
    "neutral":"neutral"
}

def detect_emotion(text):
    lower_text = text.lower()

    # Custom keyword matches first (strong override)
    if any(word in lower_text for word in ["numb", "empty", "disconnected"]):
        return "numbness"
    if any(word in lower_text for word in ["burnt out", "burnout", "exhausted", "drained"]):
        return "burnout"
    if any(word in lower_text for word in ["overthinking", "panic", "anxious"]):
        return "anxiety"
    if any(word in lower_text for word in ["unmotivated", "hopeless", "what's the point", "good for nothing", "useless", "worthless"]):
        return "motivation_loss"
    if any(word in lower_text for word in ["exhausted", "drained", "dead tired", "running on empty", "low"]):
        return "fatigue"
    if any(word in lower_text for word in ["tense", "worried", "restless"]):
        return "stress"
    if any(word in lower_text for word in ["irritated", "agitated", "losing patience", "nothing's working"]):
        return "frustration"
    if any(word in lower_text for word in ["low energy", "tired", "dowsy", "restless"]):
        return "tiredness"
    if any(word in lower_text for word in ["lost", "distraught", "drowning", "burdened"]):
        return "overwhelmed"
    if any(word in lower_text for word in ["hi", "hello", "hey", "what's up"]):
        return "greetings"
    if any(word in lower_text for word in["bye", "goodbye", "see you"]):
        return "adieus"
    if any(word in lower_text for word in["good morning", "morning"]):
        return "morning_wishes"
    if any(word in lower_text for word in["good afternoon", "good day"]):
        return "afternoon_wishes"
    if any(word in lower_text for word in["good night", "night"]):
        return "night_wishes"
    
    #If no keyword matches
    result = classifier(text)[0][0]  # Returns list of top emotion
    label = result['label'].lower()
    print(f"Detected Emotion: {label} (score: {result['score']:.2f})")
    return label_map.get(label, label)

import requests

import os
OPENROUTER_API_KEY = os.getenv("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")  # Set it in env variable instead of hardcoding

def get_coping_prompt_openrouter(user_input):
    headers = {
        "Authorization": f"Bearer {"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"}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",  # Free & supports chat
        "messages": [
            {"role": "system", "content": "You are a kind and supportive mental health assistant. Respond with short, encouraging coping suggestions."},
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    try:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        print("Error occurred:", e)
        print("Full response:", response.text)
        return "Sorry, I'm unable to provide a response right now."

# Usage (for testing, after setting env var):
print(get_coping_prompt_openrouter("I'm feeling overwhelmed and anxious."))
