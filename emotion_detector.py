# # emotion_detector.py

# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# import torch
# import torch.nn.functional as F

# # Load your trained model
# model_path = "emotion_model"
# tokenizer = AutoTokenizer.from_pretrained(model_path)
# model = AutoModelForSequenceClassification.from_pretrained(model_path)

# id2label = model.config.id2label

# def detect_emotion(text):
#     inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
#     with torch.no_grad():
#         outputs = model(**inputs)
#         probs = F.softmax(outputs.logits, dim=-1)
#         predicted_label_id = torch.argmax(probs, dim=1).item()
#         predicted_label = id2label[predicted_label_id]
#         return predicted_label
