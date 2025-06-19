import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import altair as alt

# Page title
st.title("Passive Mental Health Dashboard")
st.markdown("---")

# Load data
df = pd.read_csv("fused_scores.csv")

# Select first user for now
user_data = df.iloc[0]

# Extract scores
typing = user_data['typing_score']
voice = user_data['voice_score']
screen = user_data['screen_score']

# Calculate burnout score
burnout_score = round(typing * 0.3 + voice * 0.4 + screen * 0.3, 2)


# Create two columns
# left_col, right_col = st.columns([1, 2])  # Wider right column for chart
left_col, spacer, right_col = st.columns([1, 0.5, 2])  # Adjust middle value to increase gap


# LEFT COLUMN: Scores stacked
with left_col:
   # Display scores
    st.markdown("<div style='padding: 10px;'>Individual Fatigue Scores</div>", unsafe_allow_html=True)
    st.write(f"Typing Score: {typing}")
    st.write(f"Voice Score: {voice}")
    st.write(f"Screen Score: {screen}")

    st.markdown("---")
    
    # Show result
    st.subheader("Burnout Score")
    st.metric("Overall Score (0–5)", burnout_score)
    
    # Show suggestion
    if burnout_score > 4:
       st.error("High burnout risk! Please take a break.")
    elif burnout_score > 2.5:
        st.warning("Moderate fatigue. Monitor your workload.")
    else:
        st.success("You're doing great! Keep going.")

# RIGHT COLUMN: SHAP-style bar chart
with right_col:
    st.markdown("### SHAP-style Breakdown")
    
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
        height=400,
        xaxis_title="Modality",
        yaxis_title="Contribution Score",
        margin=dict(l=30, r=40, t=30, b=30),
        template="simple_white"
    )

    st.plotly_chart(fig, use_container_width=True)


    
    

# Existing code here (data loading, burnout score, etc.)

# Divider
st.markdown("---")
st.header("Mental Health Support Chatbot")
st.write("Feel free to share")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "chat_input" not in st.session_state:
        st.session_state.chat_input=""

# Function to generate response
def get_bot_response(user_input):
    user_input = user_input.lower()
    if "stress" in user_input or "devastated" in user_input:
        return "It's okay to feel stressed. Try taking deep breaths or a short break."
    elif "anxious" in user_input or "anxiety" in user_input:
        return "Anxiety can be tough. Try grounding techniques like naming 5 things you see around you."
    elif "sad" in user_input or "depressed" in user_input:
        return "You're not alone. It might help to talk to a friend or a counselor."
    elif "tired" in user_input or "burnout" in user_input:
        return "Burnout is real. Consider taking short breaks or talking to someone about your workload."
    elif "angry" in user_input or "rage" in user_input:
        return "That sounds really frustrating. It's okay to feel upset sometimes. Feel free to reach out."
    elif "afraid" in user_input or "fear" in user_input:
        return "Don't worry. Your feelings are safe here. What's making you feel this way?"
    elif "not okay" in user_input or "low" in user_input or "drained" in user_input:
        return "I'm sorry you have to go through this but opening up can help you a lot. Always there for help." 
    elif "happy" in user_input or "relaxed" in user_input:
        return "That's amazing to hear! Wanna tell more about your day?"
    else:
        return "I'm here for you if you feel like sharing more about how you're feeling."

# Chatbot input placeholder options
placeholder_options = [
    "How do you feel today?",
    "You can tell me anything.",
    "Need a break?",
    "Feeling okay?",
    "What’s on your mind?"
]

# Pick one randomly on each run
if "placeholder" not in st.session_state:
    st.session_state.placeholder = random.choice(placeholder_options)


# Callback to process input and clear it
def handle_input():
    user_input = st.session_state.chat_input
    if user_input:
        st.session_state.chat_history.append(f"You: {user_input}")
        bot_response= get_bot_response(user_input)
        st.session_state.chat_history.append(f"Bot: {bot_response}'")
    st.session_state.chat_input = ""  # Auto-clear


# Display chat history
for msg in st.session_state.chat_history:
    st.write(msg)

# Input field with auto-clear on enter
st.text_input("Type your message:",
              key="chat_input", 
              on_change=handle_input, 
              placeholder=st.session_state.placeholder)


