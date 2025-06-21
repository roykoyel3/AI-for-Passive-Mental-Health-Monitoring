import streamlit as st 
import random
from coping_prompts import get_coping_prompt
# from emotion_detector import detect_emotion

def show_chatbot():
    st.header("Mental Health Support Chatbot !!")

# Initialize session state for chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "chat_input" not in st.session_state:
        st.session_state.chat_input=""

# Coping Prompt to generate response
    # def get_bot_response(user_input):
    #     user_input = user_input.lower()
    #     if "stress" in user_input or "devastated" in user_input:
    #         return "It's okay to feel stressed. Try taking deep breaths or a short break."
    #     elif "anxious" in user_input or "anxiety" in user_input:
    #         return "Anxiety can be tough. Try grounding techniques like naming 5 things you see around you."
    #     elif "sad" in user_input or "depressed" in user_input:
    #         return "You're not alone. It might help to talk to a friend or a counselor."
    #     elif "tired" in user_input or "burnout" in user_input:
    #         return "Burnout is real. Consider taking short breaks or talking to someone about your workload."
    #     elif "angry" in user_input or "rage" in user_input:
    #         return "That sounds really frustrating. It's okay to feel upset sometimes. Feel free to reach out."
    #     elif "afraid" in user_input or "fear" in user_input:
    #         return "Don't worry. Your feelings are safe here. What's making you feel this way?"
    #     elif "not okay" in user_input or "low" in user_input or "drained" in user_input:
    #         return "I'm sorry you have to go through this but opening up can help you a lot. Always there for help." 
    #     elif "happy" in user_input or "relaxed" in user_input:
    #         return "That's amazing to hear! Wanna tell more about your day?"
    #     else:
    #         return "I'm here for you if you feel like sharing more about how you're feeling."
    

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
            bot_response= get_coping_prompt(user_input)
            st.session_state.chat_history.append(f"Bot: {bot_response}'")
        st.session_state.chat_input = ""  # Auto-clear


# Display chat history
    for msg in st.session_state.chat_history:
        st.write(msg)

# Input field with auto-clear on enter
    user_input=st.text_input("Type your message:",
                key="chat_input", 
                on_change=handle_input, 
                placeholder=st.session_state.placeholder)
    
    # user_input = st.text_input("How are you feeling?")
    # emotion = "anxiety"
    response = get_coping_prompt(user_input)
