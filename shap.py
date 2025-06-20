import streamlit as st 
import plotly.graph_objects as go



def shap(typing, voice, screen):

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
