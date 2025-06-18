import streamlit as st
import pandas as pd

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
st.write(f"🧠 Typing Score: {typing}")
st.write(f"🗣 Voice Score: {voice}")
st.write(f"🖥 Screen Score: {screen}")

# Calculate burnout score
burnout_score = round(typing * 0.3 + voice * 0.4 + screen * 0.3, 2)

# Show result
st.subheader("🔥 Burnout Score")
st.metric("Overall Score (0–5)", burnout_score)

# Show suggestion
if burnout_score > 4:
    st.error("High burnout risk! Please take a break.")
elif burnout_score > 2.5:
    st.warning("Moderate fatigue. Monitor your workload.")
else:
    st.success("You're doing great! Keep going. 💪")