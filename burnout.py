import streamlit as st 
import plotly.graph_objects as go 

def get_burnout(burnout_score):
    fig = go.Figure(go.Bar(
        x=[burnout_score],
       # y=["Burnout Score"],
        orientation='h',
        marker=dict(color='#835bd3'),
        width=0.4,
        text=[f"{burnout_score:.2f} / 5"],
        textposition='inside'
    ))
    
    fig.update_layout(
        height=150,
        width=2000,
        xaxis_title="Burnout Score",
        yaxis_title="Range",
        margin=dict(l=20, r=20, t=20, b=20),
        template="simple_white"
    )
    
    st.plotly_chart(fig, use_container_width=False)
    
def get_sugg(burnout_score):
    if burnout_score > 4:
        st.error("High burnout risk! Please take a break.")
    elif burnout_score > 2.5:
        st.warning("Moderate fatigue. Monitor your workload.")
    else:
        st.success("You're doing great! Keep going.")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load data
df = pd.read_csv("fused_scores.csv")
X = df[['typing_score', 'voice_score', 'screen_score']]
y = df['burnout_score']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Model
regressor = RandomForestRegressor(random_state=42)
regressor.fit(X_train, y_train)

# Evaluation
y_pred = regressor.predict(X_test) # Predicted Burnout score
print(y_pred)
print("RMSE:", mean_squared_error(y_test, y_pred)) # How close the predicted burnout scores are to the actual ones
print("R² Score:", r2_score(y_test, y_pred)) #  How much of the variation in burnout scores is explained by the model
