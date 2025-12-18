Passive Mental Health Monitoring – AI Project Portfolio

This repository contains an AI-based burnout detection and mental health support system, built using passive digital behavior signals.
The project focuses on multi-modal fatigue analysis, explainable AI, and real-time user support, implemented as an interactive dashboard.

🔹 Project Overview

Detects burnout using typing, voice, and screen behavior

Uses machine learning for burnout score prediction

Provides explainable insights using SHAP

Includes a mental health support chatbot

Designed for early detection and user-centric monitoring

🔹 Core Modules
 Fatigue Signal Processing
Module	Description
Typing Fatigue	Keystroke-based behavioral fatigue score
Voice Fatigue	Vocal signal–based fatigue indicators
Screen Fatigue	Screen usage and interaction patterns
 Burnout Prediction Model
Component	Description
Feature Fusion	Normalization + weighted combination
ML Model	Random Forest Regressor
Output	Continuous burnout score
Evaluation	RMSE and R² score
 Dashboard & Visualization
Feature	Description
User & Date Selection	Personalized monitoring
Circular Fatigue Charts	Modality-wise fatigue percentages
Burnout Score Bar	Overall mental fatigue level
Contribution Analysis	Feature impact visualization
Trend Analysis	Burnout distribution across users
Clustering	Grouping users with similar fatigue patterns
 Explainable AI (SHAP)
Visualization	Purpose
Summary Plot	Global feature importance
Individual Plot	User-specific burnout explanation
Contribution View	Positive/negative feature impact
💬 Mental Health Support Chatbot
Feature	Description
Emotion Detection	Text-based emotion classification
Coping Prompts	Manually designed supportive responses
Exercises & Resources	Calming activities and videos
Fallback AI	Ensures meaningful replies in edge cases

 Supportive tool only — not for diagnosis.

 Tools & Technologies
Category	Tools
Programming	Python
ML	scikit-learn
Explainability	SHAP
Dashboard	Streamlit
Data Handling	Pandas, NumPy
Visualization	Matplotlib, Plotly
 Key Learning Outcomes

Multi-modal feature fusion for ML systems

Practical application of explainable AI

End-to-end dashboard development

User-centric AI design for mental health

Model interpretation and visualization
