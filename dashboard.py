import os
os.environ["STREAMLIT_WATCHER_TYPE"]="none"
import streamlit as st
st.set_page_config(layout="wide")
from fatigue_charts import show_fatigues
from scores import get_user, get_score, burnout
from shap_analysis import get_shap
from burnout import get_burnout
from gui import get_gui

# Page title
st.markdown(
    "<h1 style='color: #866fc6;'>Passive Mental Health Dashboard</h1>",
    unsafe_allow_html=True
)

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
    get_shap(typing, voice, screen)
    
    
    # Show Burnout result
    st.subheader("Burnout Score")
    st.metric("Overall Score (0–5)", burnout_score)
    get_burnout(burnout_score)
        






