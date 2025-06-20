# # # # # from streamlit_lottie import st_lottie
# # # # # import requests

# # # # # # Load Lottie animation from URL
# # # # # def load_lottieurl(url):
# # # # #     r = requests.get(url)
# # # # #     if r.status_code == 200:
# # # # #         return r.json()
# # # # #     else:
# # # # #         return None

# # # # # # Example calming animation
# # # # # lottie_calm = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_tll0j4bb.json")  # relaxing animation

# # # # # st_lottie(lottie_calm, height=300, key="calm")


# # # # import streamlit as st
# # # # import pandas as pd
# # # # import plotly.graph_objects as go

# # # # # Load data
# # # # df = pd.read_csv("fused_scores.csv")
# # # # user_data = df.iloc[0]

# # # # # Extract scores
# # # # typing = user_data['typing_score']
# # # # voice = user_data['voice_score']
# # # # screen = user_data['screen_score']


# # # # # Calculate burnout score
# # # # burnout_score = round(typing * 0.3 + voice * 0.4 + screen * 0.3, 2)
# # # # # burnout = user_data['burnout_score']

# # # # # === LAYOUT START ===
# # # # st.markdown("<h2 style='color:#1d1d1f;'>🧠 Mental Health Dashboard</h2>", unsafe_allow_html=True)

# # # # # TOP ROW — METRICS
# # # # col1, col2, col3, col4 = st.columns(4)

# # # # with col1:
# # # #     st.metric("⌨️ Typing", f"{typing:.2f}")

# # # # with col2:
# # # #     st.metric("🎤 Voice", f"{voice:.2f}")

# # # # with col3:
# # # #     st.metric("📱 Screen", f"{screen:.2f}")

# # # # with col4:
# # # #     st.metric("🔥 Burnout Score", f"{burnout_score:.2f}")

# # # # # === SHAP-STYLE BAR CHART ===
# # # # st.markdown("---")
# # # # st.subheader("📊 Contribution to Burnout Score")

# # # # # Weights used
# # # # weights = {"Typing": 0.4, "Voice": 0.3, "Screen": 0.3}
# # # # contributions = {
# # # #     "Typing": weights["Typing"] * typing,
# # # #     "Voice": weights["Voice"] * voice,
# # # #     "Screen": weights["Screen"] * screen
# # # # }

# # # # # Plotly horizontal bar chart
# # # # fig = go.Figure(go.Bar(
# # # #     x=list(contributions.values()),
# # # #     y=list(contributions.keys()),
# # # #     orientation='h',
# # # #     marker_color=['#b4ff9f', '#f9f871', '#ffa07a'],
# # # #     text=[f"{v:.2f}" for v in contributions.values()],
# # # #     textposition="outside"
# # # # ))

# # # # fig.update_layout(
# # # #     height=300,
# # # #     template="simple_white",
# # # #     xaxis_title="Weighted Impact",
# # # #     title="SHAP-like Breakdown",
# # # #     margin=dict(l=40, r=40, t=40, b=40)
# # # # )

# # # # st.plotly_chart(fig, use_container_width=True)

# # # import streamlit as st
# # # import pandas as pd
# # # import plotly.graph_objects as go

# # # # Load data
# # # df = pd.read_csv("fused_scores.csv")
# # # user_data = df.iloc[0]

# # # # Scores
# # # typing = user_data['typing_score']
# # # voice = user_data['voice_score']
# # # screen = user_data['screen_score']
# # # # burnout = user_data['burnout_score']
# # # burnout_score = round(typing * 0.3 + voice * 0.4 + screen * 0.3, 2)

# # # # === LAYOUT: LEFT = Scores, RIGHT = Bar Chart ===
# # # st.markdown("<h2 style='color:#FFFFFF;'>Mental Fatigue Dashboard</h2>", unsafe_allow_html=True)
# # # st.markdown("---")

# # # # # Create two columns
# # # # # left_col, right_col = st.columns([1, 2])  # Wider right column for chart
# # # # left_col, spacer, right_col = st.columns([1, 0.5, 2])  # Adjust middle value to increase gap


# # # # # LEFT COLUMN: Scores stacked
# # # # with left_col:
# # # #     st.markdown("### Scores")
# # # #     st.markdown(f"**Typing Score:** {typing:.2f}")
# # # #     st.markdown(f"**Voice Score:** {voice:.2f}")
# # # #     st.markdown(f"**Screen Score:** {screen:.2f}")
# # # #     st.markdown("---")
# # # #     st.markdown(f"**Burnout Score:** `{burnout_score:.2f}`", unsafe_allow_html=True)

# # # # # RIGHT COLUMN: SHAP-style bar chart
# # # # with right_col:
# # # #     st.markdown("### SHAP-style Breakdown")
    
# # # #     weights = {"Typing": 0.4, "Voice": 0.3, "Screen": 0.3}
# # # #     contributions = {
# # # #         "Typing": weights["Typing"] * typing,
# # # #         "Voice": weights["Voice"] * voice,
# # # #         "Screen": weights["Screen"] * screen
# # # #     }

# # # #     fig = go.Figure(go.Bar(
# # # #         x=list(contributions.keys()),
# # # #         y=list(contributions.values()),
# # # #         # orientation='h',
# # # #         marker_color=['#bfb3de', '#a592d8', '#8a6cd4'],
# # # #          text=[
# # # #         f"Modality: {modality} | Contribution: {score:.2f}"
# # # #         for modality, score in contributions.items()
# # # #     ],
# # # #         textposition="outside"
# # # #     ))

# # # #     fig.update_layout(
# # # #         height=400,
# # # #         xaxis_title="Modality",
# # # #         yaxis_title="Contribution Score",
# # # #         margin=dict(l=30, r=40, t=30, b=30),
# # # #         template="simple_white"
# # # #     )

# # # #     st.plotly_chart(fig, use_container_width=True)

# # # import plotly.graph_objects as go

# # # def draw_score_gauge(score, label):
# # #     fig = go.Figure(go.Indicator(
# # #         mode = "gauge+number+delta",
# # #         value = score,
# # #         domain = {'x': [0, 1], 'y': [0, 1]},
# # #         title = {'text': label},
# # #         gauge = {
# # #             'axis': {'range': [0, 5]},
# # #             'bar': {'color': "#a592d8"},
# # #             'steps': [
# # #                 {'range': [0, 2.5], 'color': "#e0d9f5"},
# # #                 {'range': [2.5, 5], 'color': "#bfb3de"}
# # #             ],
# # #         }
# # #     ))
# # #     fig.update_layout(height=250, margin=dict(t=40, b=0, l=0, r=0))
# # #     return fig
# # # col1, col2= st.columns(2)
# # # with col1:
# # #     st.plotly_chart(draw_score_gauge(typing, "Typing Score"), use_container_width=True)
# # #     st.plotly_chart(draw_score_gauge(voice, "Voice Score"), use_container_width=True)
# # #     st.plotly_chart(draw_score_gauge(screen, "Screen Score"), use_container_width=True)

# from streamlit_echarts import st_echarts
# import streamlit as st
# import pandas as pd

# # st.markdown("""
# #     <style>
# #     .score-card {
# #         background: linear-gradient(160deg, #e0d9f5, #d0e0f7);
# #         padding: 20px;
# #         border-radius: 20px;
# #         text-align: center;
# #         box-shadow: 0 2px 8px rgba(0,0,0,0.05);
# #         margin border: 50px;
# #     }
# #     </style>
# # """, unsafe_allow_html=True)

# def circular_progress_chart(score: float, label: str, color="#a592d8"):
#     option = {
#         "title": {
#             "text": f"{int(score * 20)}%",
#             "left": "center",
#             "top": "45%",
#             "textStyle": {
#                 "fontSize": 24,
#                 "fontWeight": "bold",
#                 "color": "#2e2e2e",
#             },
#         },
#         "series": [
#             {
#                 "type": "pie",
#                 "radius": ["70%", "90%"],
#                 "center": ["50%", "50%"],
#                 "avoidLabelOverlap": False,
#                 "startAngle": 90,
#                 "label": {"show": False},
#                 "data": [
#                     {"value": score, "name": label, "itemStyle": {"color": color}},
#                     {"value": 5 - score, "name": "", "itemStyle": {"color": "#f0f0f0"}},
#                 ]
#             }
#         ],
#         "graphic": [
#             {
#                 "type": "text",
#                 "left": "center",
#                 "top": "30%",
#                 "style": {
#                     "text": label,
#                     "fontSize": 16,
#                     "fill": "#555"
#                 }
#             }
#         ]
#     }

#     st_echarts(options=option, height="220px")
#     #  # Wrap in styled gradient card
#     # st.markdown('<div class="score-card">', unsafe_allow_html=True)
#     # st_echarts(options=option, height="230px")
#     # st.markdown('</div>', unsafe_allow_html=True)


    
# # # Load data
# # df = pd.read_csv("fused_scores.csv")

# # # Select first user for now
# # user_data = df.iloc[0]

# # # Extract scores
# # typing = user_data['typing_score']
# # voice = user_data['voice_score']
# # screen = user_data['screen_score']

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.markdown('<div class="score-card">', unsafe_allow_html=True)
#     circular_progress_chart(typing, "Typing")
#     st.markdown('</div>', unsafe_allow_html=True)

# with col2:
#     st.markdown('<div class="score-card">', unsafe_allow_html=True)
#     circular_progress_chart(voice, "Voice")
#     st.markdown('</div>', unsafe_allow_html=True)

# with col3:
#     st.markdown('<div class="score-card">', unsafe_allow_html=True)
#     circular_progress_chart(screen, "Screen")
#     st.markdown('</div>', unsafe_allow_html=True)

import plotly.graph_objects as go
import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts

df = pd.read_csv("fused_scores.csv")

# Select first user for now
user_data = df.iloc[0]

# Extract scores
typing = user_data['typing_score']
voice = user_data['voice_score']
screen = user_data['screen_score']

# Calculate burnout score
burnout_score = round(typing * 0.3 + voice * 0.4 + screen * 0.3, 2)

c1, c2, c3, c4=st.columns(4)
with c1:
    st.subheader("🔥 Burnout Level")

    fig = go.Figure(go.Bar(
    x=[burnout_score],
    y=["Burnout Score"],
    orientation='h',
    marker=dict(color='#835bd3'),
    width=0.4,
    text=[f"{burnout_score:.2f} / 5"],
    textposition='outside'
    ))

    fig.add_shape(
    type="rect",
    x0=0, x1=5, y0=0, y1=1,
    line=dict(width=0),
    fillcolor="#e0e0e0",
    layer="below"
    )


    fig.add_shape(
    type="rect",
    x0=0, x1=burnout_score, y0=0, y1=1,
    line=dict(width=0),
    fillcolor="#835bd3",
    layer="above"
    )


    fig.update_layout(
    xaxis=dict(range=[0, 5]),
    height=150,
    template="simple_white",
    margin=dict(l=30, r=30, t=30, b=30)
    )

    st.plotly_chart(fig, use_container_width=True)

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
        
with c2:
    st.markdown('<div class="score-card">', unsafe_allow_html=True)
    circular_progress_chart(typing, "Typing")
    st.markdown('</div>', unsafe_allow_html=True)
    
with c3:
    st.markdown('<div class="score-card">', unsafe_allow_html=True)
    circular_progress_chart(voice, "Voice")
    st.markdown('</div>', unsafe_allow_html=True)
    

with c4:
    st.markdown('<div class="score-card">', unsafe_allow_html=True)
    circular_progress_chart(screen, "Screen")
    st.markdown('</div>', unsafe_allow_html=True)
    
    
    

## dark and light theme
# theme = st.selectbox("Choose Theme", ["Light", "Dark"])
# if theme == "Dark":
#     bg_color = "#0e1117"
#     text_color = "#fafafa"
#     chart_template = "plotly_dark"
# else:
#     bg_color = "#ffffff"
#     text_color = "#262730"
#     chart_template = "plotly_white"
# fig.update_layout(template=chart_template)
# st.markdown(f"<div style='color:{text_color}; background:{bg_color}; padding:10px;'>Your content here</div>", unsafe_allow_html=True)

# import glob
# import os

# # Find all fused_scores_*.csv files
# files = glob.glob("fused_scores_*.csv")

# if not files:
#     st.error("No data files found!")
# else:
#     latest_file = max(files, key=os.path.getmtime)
#     df = pd.read_csv(latest_file)
#     st.success(f"📂 Loaded latest scores from: `{latest_file}`")

# ##( All the scores collected from three different persons, is to append 
# # in a single csv file with a column introduced as timestamp. here the fusion 
# # is done but if we need to check the individual scores and burnout score
# # thshap and all, we will select according to the timestamp of the csv file,
# # the latest data entries from the csv file. Otherwise we will keep an option 
# # to manually select the particular user with the help of user id and the timestamp)

# import pandas as pd

# # Load full data
# df_all = pd.read_csv("fused_scores_all.csv")

# # Convert timestamp column to datetime
# df_all['timestamp'] = pd.to_datetime(df_all['timestamp'])

# # Option A: Get latest data for all users
# latest_data = df_all.sort_values('timestamp').groupby('user_id').tail(1)

# # Option B: Get latest entry overall (any user)
# latest_data = df_all.sort_values('timestamp').iloc[-1:]

# # For example: show the latest for 'User A'
# user_data = latest_data[latest_data['user_id'] == 'User A'].iloc[0]

# typing = user_data['typing_score']
# voice = user_data['voice_score']
# screen = user_data['screen_score']
# burnout = user_data['burnout_score']

st.markdown("""
    <style>
    body {
        background: linear-gradient(-45deg, #1e1e2f, #282c34, #1e1e2f, #2b2b3c);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    </style>
""", unsafe_allow_html=True)


