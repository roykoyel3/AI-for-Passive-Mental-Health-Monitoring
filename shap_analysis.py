# import streamlit as st 
# import plotly.graph_objects as go



# def shap(typing, voice, screen):

#     #Defining weights
#     weights = {"Typing": 0.3,
#             "Voice": 0.4, 
#             "Screen": 0.3}
    
#     #Calculated weighted contributions(SHAP-style)
#     contributions = {
#         "Typing": weights["Typing"] * typing,
#         "Voice": weights["Voice"] * voice,
#         "Screen": weights["Screen"] * screen
#     }

#     fig = go.Figure(go.Bar(
#         x=list(contributions.keys()),
#         y=list(contributions.values()),
#         # orientation='h',
#         marker_color=['#bfb3de', '#a592d8', '#8a6cd4'],
#          text=[
#         f"Modality: {modality} | Contribution: {score:.2f}"
#         for modality, score in contributions.items()
#     ],
#         textposition="outside"
#     ))

#     fig.update_layout(
#         height=450,
#         xaxis_title="Modality",
#         yaxis_title="Contribution Score",
#         margin=dict(l=30, r=40, t=30, b=30),
#         template="simple_white"
#     )

#     st.plotly_chart(fig, use_container_width=True)


import shap
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Sample data
# data = pd.DataFrame({
#     "typing_score": [0.2, 0.6, 0.4, 0.9, 0.1],
#     "voice_score": [0.5, 0.7, 0.2, 0.4, 0.8],
#     "screen_score": [0.7, 0.3, 0.9, 0.6, 0.4]
# })
# target = np.array([0.6, 0.8, 0.4, 0.9, 0.5])  # burnout score

# Data load
data=pd.read_csv("fused_scores.csv")

# Split features and target
x= data.drop(columns=['burnout_score','user_id','date']) #Features
y= data['burnout_score']  #Target
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor()
model.fit(x_train, y_train)

# SHAP Explainer
explainer = shap.Explainer(model.predict, x_train)
shap_values = explainer(x_train)

# STREAMLIT INTEGRATION
st.title("SHAP Analysis for Burnout Prediction")

# SHAP Summary Plot (global explanation)
st.subheader("📊 SHAP Summary Plot")
fig_summary, ax = plt.subplots()
shap.summary_plot(shap_values, x_train, show=False)
st.pyplot(fig_summary)

# SHAP Force Plot (individual prediction explanation)
st.subheader("⚡ Individual Prediction Force Plot")
index = st.slider("Select a user index", 0, len(data)-1, 0)
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
# plt.show()
# st.pyplot(fig_force)

# SHAP Bar Plot
st.subheader("🔍 Feature Importance Bar Plot")
shap.plots.bar(shap_values)
st.pyplot(bbox_inches='tight')
