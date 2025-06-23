import streamlit as st 
from streamlit_echarts import st_echarts
from scores import get_score, get_user, burnout
from fatigue_charts import circular_progress_chart
from gui import get_gui
from burnout import get_burnout, get_sugg

get_gui()

user_data=get_user()
typing, voice, screen= get_score(user_data)
burnout_score=burnout(typing, screen, voice)

st.markdown(
    "<h1 style='color: #866fc6;'>Fatigue Analysis</h1>",
    unsafe_allow_html=True
)

st.markdown("---")
    
st.header("Fatigue Scores")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader(" Typing Score")
    st.markdown('<div class="score-card">', unsafe_allow_html=True)
    circular_progress_chart(typing, "Typing")
    st.markdown('</div>', unsafe_allow_html=True)
    
with col2:
    st.subheader(" Voice Score")
    st.markdown('<div class="score-card">', unsafe_allow_html=True)
    circular_progress_chart(voice, "Voice")
    st.markdown('</div>', unsafe_allow_html=True)
    
with col3:
    st.subheader(" Screen Score")
    st.markdown('<div class="score-card">', unsafe_allow_html=True)
    circular_progress_chart(screen, "Screen")
    st.markdown('</div>', unsafe_allow_html=True)

st.header("Burnout Score") 
st.text("The burnout score is a single metric that reflects your current mental fatigue level based on your typing, voice, and screen activity patterns.")   
get_burnout(burnout_score)

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
st.markdown(y_pred)
rmse= mean_squared_error(y_test,y_pred)
st.markdown(f"RMSE:{rmse}") # How close the predicted burnout scores are to the actual ones
rr=r2_score(y_test,y_pred)
st.markdown(f"R² Score:{rr}") #  How much of the variation in burnout scores is explained by the model


st.header("Suggestion For You:")
get_sugg(burnout_score)
