import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts

def circular_progress_chart(score: float, label: str, color="#6b50b5"):
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
    
def show_fatigues(typing,voice,screen):
    st.markdown('<div class="score-card">', unsafe_allow_html=True)
    circular_progress_chart(typing, "Typing")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="score-card">', unsafe_allow_html=True)
    circular_progress_chart(voice, "Voice")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="score-card">', unsafe_allow_html=True)
    circular_progress_chart(screen, "Screen")
    st.markdown('</div>', unsafe_allow_html=True)



