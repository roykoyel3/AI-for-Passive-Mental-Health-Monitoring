import streamlit as st
import pandas as pd

# Page title
st.title("Passive Mental Health Dashboard")

# Load data
df = pd.read_csv("fused_scores.csv")

# Select user (for now, assume single user or use dropdown)
user_data = df.iloc[0]  # default: first user

# Extract scores
typing = user_data['typing_score']
voice = user_data['voice_score']
screen = user_data['screen_score']

# Show individual scores
st.subheader("Individual Fatigue Scores")
st.write(f"🧠 Typing Score: {typing}")
st.write(f"🗣️ Voice Score: {voice}")
st.write(f"🖥️ Screen Score: {screen}")

# Fusion logic (custom weights)
burnout_score = round(typing * 0.3 + voice * 0.4 + screen * 0.3, 2)

# Display final burnout score
st.subheader("🔥 Burnout Score")
st.metric("Overall Score (0–5)", burnout_score)

# Interpretation message
if burnout_score > 4:
    st.error("High burnout risk! Please take a break.")
elif burnout_score > 2.5:
    st.warning("Moderate fatigue. Monitor your workload.")
else:
    st.success("You're doing great! Keep going. 💪")
