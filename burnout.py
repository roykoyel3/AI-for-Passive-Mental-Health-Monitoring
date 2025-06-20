import streamlit as st 
import plotly.graph_objects as go 

def get_burnout(burnout_score):
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
    
def get_sugg(burnout_score):
    if burnout_score > 4:
        st.error("High burnout risk! Please take a break.")
    elif burnout_score > 2.5:
        st.warning("Moderate fatigue. Monitor your workload.")
    else:
        st.success("You're doing great! Keep going.")