import os
os.environ["STREAMLIT_WATCHER_TYPE"]="none"
import streamlit as st 
import random
import sys
sys.path.append('C:/Users/hp/OneDrive/Desktop/AI for Passive Mental Health Monitoring/')
from coping_prompts import get_coping_prompt

# from coping_prompts import get_coping_prompt
from gui import get_gui
from emotions import detect_emotion
# from emotion_detector import detect_emotion

get_gui()

def show_chatbot():
    st.title("        ")
    st.markdown(
    "<h1 style='color: #866fc6;'>Mental Health Support Chatbot!!</h1>",
    unsafe_allow_html=True
)


# Initialize session state for chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "chat_input" not in st.session_state:
        st.session_state.chat_input=""
      
# Callback to process input and clear it
    def handle_input():
        user_input = st.session_state.chat_input
        if user_input:
            st.session_state.chat_history.append(f"You: {user_input}")
            emotion=detect_emotion(user_input)
            bot_response=get_coping_prompt(emotion)
            st.session_state.chat_history.append(f"Bot: {bot_response}'")
        st.session_state.chat_input = ""  # Auto-clear

# Display chat history
    for msg in st.session_state.chat_history:
        st.write(msg)

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

# Input field with auto-clear on enter
    user_input=st.text_input("Type your message:",
                key="chat_input", 
                on_change=handle_input, 
                placeholder=st.session_state.placeholder)
    
    
show_chatbot()