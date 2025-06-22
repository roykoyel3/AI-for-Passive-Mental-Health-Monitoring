import streamlit as st 
from streamlit_echarts import st_echarts
from scores import get_score, get_user, burnout
from fatigue_charts import circular_progress_chart
from gui import get_gui
from burnout import get_burnout, get_sugg

get_gui()

user_data=get_user()
typing, voice, screen= get_score(user_data)
burnout_score=burnout(typing, screen, voice)

st.markdown(
    "<h1 style='color: #866fc6;'>Fatigue Analysis</h1>",
    unsafe_allow_html=True
)

st.markdown("---")
    
st.header("Fatigue Scores")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader(" Typing Score")
    st.markdown('<div class="score-card">', unsafe_allow_html=True)
    circular_progress_chart(typing, "Typing")
    st.markdown('</div>', unsafe_allow_html=True)
    
with col2:
    st.subheader(" Voice Score")
    st.markdown('<div class="score-card">', unsafe_allow_html=True)
    circular_progress_chart(voice, "Voice")
    st.markdown('</div>', unsafe_allow_html=True)
    
with col3:
    st.subheader(" Screen Score")
    st.markdown('<div class="score-card">', unsafe_allow_html=True)
    circular_progress_chart(screen, "Screen")
    st.markdown('</div>', unsafe_allow_html=True)

st.header("Burnout Score") 
st.text("The burnout score is a single metric that reflects your current mental fatigue level based on your typing, voice, and screen activity patterns.")   
get_burnout(burnout_score)

st.header("Suggestion For You:")
get_sugg(burnout_score)
