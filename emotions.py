# from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# # Use slow tokenizer explicitly
# model_name = "mrm8488/t5-base-finetuned-emotion"
# tokenizer = AutoTokenizer.from_pretrained("t5-base", use_fast=False)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# model2 = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

# # Optional: label mapping if needed (tweak if your coping_prompt_library uses slightly different labels)
# label_map = {
#     'joy': 'joy',
#     'sad': 'sadness',
#     'anger': 'anger',
#     'surprise': 'surprise',
#     'fear': 'fear',
#     'love': 'love',
#     'thankful': 'gratitude',
#     'neutral': 'neutral',
#     'anxious':'anxiety'
# }

# def detect_emotion(text):
#     output = model2(text)[0]  # e.g., {'generated_text': 'sad'}
#     result = output['generated_text'].strip().lower()
#     print("Raw model output:", result)  # Or st.write in Streamlit

#     # Map to standard label
#     return label_map.get(result, result)

from transformers import pipeline

# Load the pretrained emotion classification model
classifier = pipeline("text-classification", model="nateraw/bert-base-uncased-emotion")

# Optional: Mapping to match your coping_prompt_library if needed
label_map = {
    "sadness": "sadness",
    "joy": "joy",
    "love": "love",
    "anger": "anger",
    "fear": "fear",
    "surprise": "surprise",
    "neutral": "neutral"
}

def detect_emotion(text):
    negation_phrases = {
    "not sad": "neutral",
    "not angry": "neutral",
    "not anxious": "neutral",
    "not scared": "neutral",
    }

    text_lower = text.lower()
    for phrase, label in negation_phrases.items():
        if phrase in text_lower:
            return label

    result = classifier(text)[0]  # Output: {'label': 'joy', 'score': 0.98}
    label = result['label'].lower()
    print(f"Detected Emotion: {label} (score: {result['score']:.2f})")
    return label_map.get(label, label)  # fallback if label isn't in map
