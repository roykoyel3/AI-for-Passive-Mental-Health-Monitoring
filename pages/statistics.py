import sys
import os

# Add the main project folder to system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st 
import plotly.graph_objects as go
from scores import get_score, get_user
from shap import shap

user_data=get_user()
typing, voice, screen= get_score(user_data)

st.title("SHAP Explanation Statistics")
st.markdown("(SHapley Additive exPlanations)")

st.markdown("---")

# SHAP-chart
shap(typing, voice, screen)

st.markdown("The analysis below breaks down how different aspects of your digital behaviour- typing patterns, voice cues and screen engagement- have contributed to your current fatigue.")
st.markdown("---")

# Shap explanation
scores={
    "Typing Fatigue": typing,
    "Voice Fatigue": voice,
    "Screen Fatigue": screen
}

st.header("Individual Analysis:")

# Individual explanations
explanation=""
if typing > 0.6:
    typing_exp = "Your typing behavior suggests elevated mental load or fatigue.\n "
elif typing < 0.3:
    typing_exp = "Your typing data indicates a relatively calm and steady interaction.\n "
else:
    typing_exp = "Your typing activity appears moderately strained.\n "

if voice > 0.6:
    voice_exp = "\nVoice tone analysis indicates stress or emotional exhaustion.\n "
elif voice < 0.3:
    voice_exp = "Your voice signals show signs of emotional stability and calm.\n "
else:
    voice_exp = "Your voice tone shows some fluctuations that could reflect strain.\n "

if screen > 0.6:
    screen_exp = "\nScreen interaction patterns suggest signs of digital overload.\n "
elif screen < 0.3:
    screen_exp = "Screen usage seems balanced and healthy.\n "
else:
    screen_exp = "Your screen behavior is moderately active and could trend toward fatigue.\n "

# Combine individual explanations
st.markdown(f"**Typing Score:{typing}**\n \n{typing_exp}\n **Voice Score:{voice}**\n {voice_exp}\n **Screen Score:{screen}**\n {screen_exp}\n")


top_factor= max(scores, key=scores.get)

st.subheader(f"Your highest contribution factor to fatigue appears to be **{top_factor}**.")