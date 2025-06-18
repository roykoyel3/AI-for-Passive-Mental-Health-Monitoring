import streamlit as st
import pandas as pd
import random

# Page title
st.title("Passive Mental Health Dashboard")

# Load data
df = pd.read_csv("fused_scores.csv")

# Select first user for now
user_data = df.iloc[0]

# Extract scores
typing = user_data['typing_score']
voice = user_data['voice_score']
screen = user_data['screen_score']

# Display scores
st.subheader("Individual Fatigue Scores")
st.write(f"Typing Score: {typing}")
st.write(f"Voice Score: {voice}")
st.write(f"Screen Score: {screen}")

# Calculate burnout score
burnout_score = round(typing * 0.3 + voice * 0.4 + screen * 0.3, 2)

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
    if "stress" in user_input:
        return "It's okay to feel stressed. Try taking deep breaths or a short break."
    elif "anxious" in user_input or "anxiety" in user_input:
        return "Anxiety can be tough. Try grounding techniques like naming 5 things you see around you."
    elif "sad" in user_input or "depressed" in user_input:
        return "You're not alone. It might help to talk to a friend or a counselor."
    elif "tired" in user_input or "burnout" in user_input:
        return "Burnout is real. Consider taking short breaks or talking to someone about your workload."
    else:
        return "I'm here for you. Try sharing more about how you're feeling."

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
