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


# Page title
st.title("Passive Mental Health Dashboard")
st.markdown("---")



with st.sidebar:
    st.header("Navigation")
    st.button("Home")
    st.button("Statistics")
    st.button("Burnout Analysis")
    st.button("Chatbot")
    

# Custom CSS
st.markdown("""
    <style>
        [data-testid="stSidebar"]{
            background-color:transparent !important; 
        }
        
        /* Main sidebar style */
        [data-testid="stSidebar"] > div:first-child {
            background-color: #0e1117 !important; /* semi-transparent bg */
            border-radius: 20px;
            margin: 50px 10px 50px 10px;
            padding: 50px 10px;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            box-shadow: 0 0 7px rgba(85, 0, 255, 0.4);  /* blue-purple soft glow */
            border: 1px solid rgba(180, 100, 255, 0.2);  /* soft tinted border */
            transition: all 0.3s ease-in-out;
        }
        
        /* On hover: slight scale and brighter glow */
        [data-testid="stSidebar"] > div:first-child:hover {
            transform: scale(1.01);
            box-shadow: 0 0 10px rgba(130, 80, 255, 0.6);
        }
        
        /* Make sidebar full height flex container */
        [data-testid="stSidebar"] > div:first-child {
            display: flex;
            flex-direction: column;
            justify-content: center;  /* Center vertically */
            height: 100vh;
        }
          
        /* Sidebar heading */
        .css-1v0mbdj h2 {
            font-size: 24px;
            color: white;
        }

        /* Button style (optional tweak) */
        .stButton>button {
            border-radius: 12px;
            background-color: #2c2f36;
            color: white;
            padding: 10px 20px;
            margin: 5px 0px;
            transition: 0.3s ease-in-out;
            border: 1px solid #444;
        }

        .stButton>button:hover {
            background-color: #4b4e56;
            transform: scale(1.02);
            border: 1px solid #888;
        
        [data-testid="stSidebar"] > div:first-child {
            display: flex;
            flex-direction: column;
            justify-content: center;
            height: 100vh;
        }
        
    </style>
""", unsafe_allow_html=True)

    

left,right=st.columns(2)

with left:
    # Get the latest user details
    user_data=get_user()
    
# Extract scores
typing, voice, screen = get_score(user_data)
    
# Calculate burnout score
burnout_score=burnout(typing, voice, screen)

# Create two columns
# left_col, right_col = st.columns([1, 2])  # Wider right column for chart
left_col, spacer, right_col= st.columns([1, 0.5, 2])  # Adjust middle value to increase gap

# LEFT COLUMN: Scores stacked
with left_col:
    
    st.markdown("### Fatigue Scores")
    
    # Fatigue_scores chart
    show_fatigues(typing,voice,screen)
    
    
# RIGHT COLUMN: SHAP-style bar chart
with right_col:
    
    st.markdown("### Contribution-Explanation")
    
    #Defining weights
    weights = {"Typing": 0.3,
               "Voice": 0.4, 
               "Screen": 0.3}
    
    #Calculated weighted contributions(SHAP-style)
    contributions = {
        "Typing": weights["Typing"] * typing,
        "Voice": weights["Voice"] * voice,
        "Screen": weights["Screen"] * screen
    }

    fig = go.Figure(go.Bar(
        x=list(contributions.keys()),
        y=list(contributions.values()),
        # orientation='h',
        marker_color=['#bfb3de', '#a592d8', '#8a6cd4'],
         text=[
        f"Modality: {modality} | Contribution: {score:.2f}"
        for modality, score in contributions.items()
    ],
        textposition="outside"
    ))

    fig.update_layout(
        height=450,
        xaxis_title="Modality",
        yaxis_title="Contribution Score",
        margin=dict(l=30, r=40, t=30, b=30),
        template="simple_white"
    )

    st.plotly_chart(fig, use_container_width=True)
    
    # Show result
    st.subheader("Burnout Score")
    st.metric("Overall Score (0–5)", burnout_score)
    
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



st.subheader("Suggestion for you:")
# Show suggestion
if burnout_score > 4:
    st.error("High burnout risk! Please take a break.")
elif burnout_score > 2.5:
    st.warning("Moderate fatigue. Monitor your workload.")
else:
    st.success("You're doing great! Keep going.")
    

# Existing code here (data loading, burnout score, etc.)

# Chatbot
st.markdown("---")
show_chatbot()


