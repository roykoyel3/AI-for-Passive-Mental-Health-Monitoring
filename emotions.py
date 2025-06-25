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
    result = classifier(text)[0][0]  # Returns list of top emotion
    label = result['label'].lower()
    print(f"Detected Emotion: {label} (score: {result['score']:.2f})")
    return label_map.get(label, label)

