import streamlit as st 
import pandas as pd 

def get_user():
    # Load data
    df = pd.read_csv("fused_scores.csv")
    # # Show user selector
    # user_list=df['user_id'].unique().tolist()
    # selected_user=st.selectbox("Select a user", user_list, key="user_selectbox")

    # # Get that user's row
    # user_data = df[df['user_id'] == selected_user].iloc[0]

    # Select first user for now
    user_data = df.iloc[0]

    return user_data


def get_score(user_data):
    # Extract scores
    typing = user_data['typing_score']
    voice = user_data['voice_score']
    screen = user_data['screen_score']
    
    return typing, voice, screen


def burnout(typing,voice,screen):
    # Calculate burnout score
    burnout_score = round(typing * 0.3 + voice * 0.4 + screen * 0.3, 2)
    return burnout_score
