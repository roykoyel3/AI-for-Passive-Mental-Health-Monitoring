import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import random
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import altair as alt
from streamlit_echarts import st_echarts


# Page title
st.title("Passive Mental Health Dashboard")
st.markdown("---")

# Load data
df = pd.read_csv("fused_scores.csv")

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
    #Show user selector
    user_list=df['user_id'].unique().tolist()
    selected_user=st.selectbox("Select a user", user_list)

# Get that user's row
user_data = df[df['user_id'] == selected_user].iloc[0]

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
left_col, spacer, right_col= st.columns([1, 0.5, 2])  # Adjust middle value to increase gap

# LEFT COLUMN: Scores stacked
with left_col:
    
    st.markdown("### Fatigue Scores")
    
    def circular_progress_chart(score: float, label: str, color="#a592d8"):
        option = {
            "title": {
                "text": f"{int(score * 20)}%",
                "left": "center",
                "top": "45%",
                "textStyle": {
                    "fontSize": 24,
                    "fontWeight": "bold",
                    "color": "#2e2e2e",
                },
            },
            "series": [
                {
                    "type": "pie",
                    "radius": ["70%", "90%"],
                    "center": ["50%", "50%"],
                    "avoidLabelOverlap": False,
                    "startAngle": 90,
                    "label": {"show": False},
                    "data": [
                        {"value": score, "name": label, "itemStyle": {"color": color}},
                        {"value": 5 - score, "name": "", "itemStyle": {"color": "#f0f0f0"}},
                    ]
                }
            ],
            "graphic": [
                {
                    "type": "text",
                    "left": "center",
                    "top": "30%",
                    "style": {
                        "text": label,
                        "fontSize": 16,
                        "fill": "#555"
                    }
                }
            ]
        }

        st_echarts(options=option, height="200px")
    
    st.markdown('<div class="score-card">', unsafe_allow_html=True)
    circular_progress_chart(typing, "Typing")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="score-card">', unsafe_allow_html=True)
    circular_progress_chart(voice, "Voice")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="score-card">', unsafe_allow_html=True)
    circular_progress_chart(screen, "Screen")
    st.markdown('</div>', unsafe_allow_html=True)
    

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

# Divider
st.markdown("---")
st.header("Mental Health Support Chatbot !!")

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


# st.markdown("""
# <style>
#     .element-container {
#         border-radius: 20px;
#         box-shadow: 0px 2px 15px rgba(0, 0, 0, 0.1);
#         padding: 1.5rem;
#         background-color: #fdfdfd;
#         margin-bottom: 1rem;
#     }
# </style>
# """, unsafe_allow_html=True)