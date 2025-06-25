import sys
import os

# Add the main project folder to system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st 
import plotly.graph_objects as go
from scores import get_score, get_user
from gui import get_gui

get_gui()

st.markdown("""
    <style>
     .subtitle {
        color: #5c5c7a;
        margin-bottom: 1rem;
        font-size: 1.1rem;
    }
    </style>
            """, unsafe_allow_html=True)

user_data=get_user()
typing, voice, screen= get_score(user_data)

st.markdown(
    "<h1 style='color: #866fc6;'>SHAP Analysis for Burnout Prediction</h1>",
    unsafe_allow_html=True
)

st.markdown('<div class="subtitle">SHapley Additive exPlanations', unsafe_allow_html=True)

st.markdown("---")

import shap
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Data load
data=pd.read_csv("fused_scores.csv")

# Split features and target
x= data[['typing_score','voice_score','screen_score']] #Features
y= data['burnout_score']  #Target
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size=0.2, random_state=42)

# Train a model on full data
model= RandomForestRegressor(random_state=42)
model.fit(x,y)

# Select the most recent user (last row of csv)
latest_user=x.iloc[[-1]]

# Predict burnout score
predicted_burnout=model.predict(latest_user)[0]

# Explain prediction with SHAP
explainer= shap.Explainer(model.predict,x)
shap_values_latest= explainer(latest_user)

# Plot SHAP
st.subheader("Factors Behind Your Burnout Prediction")
st.write(f"Predicted burnout score: **{predicted_burnout:.2f}")

#Waterfall plot(SHAP for individual user)
fig, ax = plt.subplots()
shap.plots.waterfall(shap_values_latest[0], show=False)
st.pyplot(fig)  # ✅ pass the figure object explicitly
plt.clf()

# Train model
model = RandomForestRegressor().fit(x,y)
model.fit(x_train, y_train)

# SHAP Explainer
explainer = shap.Explainer(model.predict, x_train)
shap_values = explainer(x_train)

# SHAP Summary Plot (global explanation)
st.subheader("What Matters Most in Predicting Burnout")
fig_summary, ax = plt.subplots()
shap.summary_plot(shap_values, x_train, show=False)
st.pyplot(fig_summary)

# SHAP Force Plot (individual prediction explanation)
st.subheader("Understand Your Score Composition")
index = st.slider("Select a user index", 0, len(data)-1, 0) #may give an error replace data with x_train
fig_force, ax = plt.subplots(figsize=(10, 2))
with plt.rc_context({'figure.figsize': (10, 2)}):
    shap.plots.force(
        shap_values[index].base_values,
        shap_values[index].values,
        shap_values[index].data,
        matplotlib=True,
        show=False
    )
st.pyplot(plt.gcf())

# SHAP Bar Plot
st.subheader("Feature Importance Bar Plot")

# Compute mean absolute SHAP values across all samples
mean_shap = np.abs(shap_values.values).mean(axis=0)
feature_names = shap_values.feature_names
fig, ax = plt.subplots()
ax.barh(feature_names, mean_shap, color='teal')
ax.set_xlabel("Mean |SHAP value|")
ax.set_title("Global Feature Importance (Bar)")
st.pyplot(fig)

