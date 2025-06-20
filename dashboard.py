import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import random
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import altair as alt
from streamlit_echarts import st_echarts
from fatigue_charts import show_fatigues
from chatbot import show_chatbot
from scores import get_user, get_score, burnout
from shap import shap
from burnout import get_burnout, get_sugg
from gui import get_gui

# Page title
st.title("Passive Mental Health Dashboard")
st.markdown("---")

get_gui()
    

left,right=st.columns(2)

with left:
    # Get the latest user details
    user_data=get_user()
    
# Extract scores
typing, voice, screen = get_score(user_data)
    
# Calculate burnout score
burnout_score=burnout(typing, voice, screen)

# Create two columns
left_col, spacer, right_col= st.columns([1, 0.5, 2])  

# LEFT COLUMN: Scores stacked
with left_col:
    
    st.markdown("### Fatigue Scores")
    
    # Fatigue_scores chart
    show_fatigues(typing,voice,screen)
    
    
# RIGHT COLUMN: SHAP-style bar chart
with right_col:
    
    st.markdown("### Contribution-Explanation")
    shap(typing, voice, screen)
    
    
    # Show Burnout result
    st.subheader("Burnout Score")
    st.metric("Overall Score (0–5)", burnout_score)
    get_burnout(burnout_score)
        
st.subheader("Suggestion for you:")
# Show suggestion
get_sugg(burnout_score)


# Chatbot
st.markdown("---")
show_chatbot()


