import streamlit as st
from datetime import datetime
from gui import get_gui

get_gui()


# Custom CSS for theme
st.markdown("""
    <style>
    body {
        background-color: #f8f5fc;
    }
    .title {
        font-size: 2rem;
        color: #6b50b5;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        color: #5c5c7a;
        margin-bottom: 1rem;
        font-size: 1.1rem;
    }
    .stButton>button {
        background-color: #6b50b5;
        color: white;
        border-radius: 0.8rem;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Feedback Section
st.markdown('<div class="feedback-box">', unsafe_allow_html=True)
st.markdown('<div class="title">💬 We’d Love Your Feedback!</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Tell us how your experience was using the burnout dashboard. Your thoughts help us improve.</div>', unsafe_allow_html=True)

# Feedback form
with st.form("feedback_form"):
    name = st.text_input("Your Name (optional)")
    experience = st.selectbox(
        "How would you rate your experience?",
        ["🌟🌟🌟🌟🌟 - Excellent", "🌟🌟🌟🌟 - Good", "🌟🌟🌟 - Okay", "🌟🌟 - Poor", "🌟 - Very Poor"]
    )
    feedback = st.text_area("Write your feedback", height=150)
    submitted = st.form_submit_button("Submit Feedback")

    if submitted:
        # Ideally save feedback to database or file (placeholder message for now)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.success("Thank you for your feedback! 💜")

        # Optional debug info
        print("Feedback received:", {"name": name, "experience": experience, "feedback": feedback, "time": timestamp})

st.markdown("</div>", unsafe_allow_html=True)
