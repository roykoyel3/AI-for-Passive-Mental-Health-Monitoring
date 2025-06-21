# from datasets import load_dataset
# from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
# from sklearn.metrics import accuracy_score, f1_score
# import torch

# # Load EmpatheticDialogues Dataset
# dataset= load_dataset("empathetic_dialogues")

# # Preprocess: we'll use the 'utterance' as input and 'emotion' as label
# label_list= sorted(list(set(dataset['trian']['emotion'])))
# label2id= {label: i for i, label in enumerate(label_list)}
# id2label= {i:label for label, i in label2id.items()}

# def preprocess(example):
#     return{
#         "text": example["utterance"],
#         "label": label2id[example["emotion"]]
#     }

# dataset= dataset.map(preprocess)
# dataset= dataset.rename_column("text","text")
# dataset= dataset.rename_column("label","labels")
# dataset.set_format(type="torch", columns=["text","labels"])

# # Load tokenizer and model
# model_name = "distilbert-base-uncased"
# tokenizer = AutoTokenizer.from_pretrained(model_name)

# def tokenize(batch):
#     return tokenizer(batch["text"], padding=True, truncation=True)

# tokenized_dataset = dataset.map(tokenize, batched=True)

# model = AutoModelForSequenceClassification.from_pretrained(
#     model_name,
#     num_labels=len(label_list),
#     id2label=id2label,
#     label2id=label2id
# )

# # Define evaluation metrics
# def compute_metrics(pred):
#     labels = pred.label_ids
#     preds = pred.predictions.argmax(-1)
#     return {
#         "accuracy": accuracy_score(labels, preds),
#         "f1": f1_score(labels, preds, average="weighted")
#     }

# # Training arguments
# training_args = TrainingArguments(
#     output_dir="./emotion_classifier",
#     evaluation_strategy="epoch",
#     save_strategy="epoch",
#     num_train_epochs=3,
#     per_device_train_batch_size=16,
#     per_device_eval_batch_size=16,
#     logging_dir='./logs',
#     logging_steps=10,
#     load_best_model_at_end=True
# )

# trainer = Trainer(
#     model=model,
#     args=training_args,
#     train_dataset=tokenized_dataset["train"].shuffle(seed=42).select(range(10000)),  # optionally subset
#     eval_dataset=tokenized_dataset["validation"].select(range(2000)),
#     tokenizer=tokenizer,
#     compute_metrics=compute_metrics,
# )

# # Train!
# trainer.train()
# trainer.save_model("emotion_model")
# tokenizer.save_pretrained("emotion_model")