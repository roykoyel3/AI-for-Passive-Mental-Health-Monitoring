# import streamlit as st 
# import plotlty.graph_objects as go

# #Show user selector
#     user_list=df['user_id'].unique().tolist()
#     selected_user=st.selectbox("Select a user", user_list)

# # Get that user's row
# user_data = df[df['user_id'] == selected_user].iloc[0]

# # Select first user for now
# user_data = df.iloc[0]

# # Extract scores
# typing = user_data['typing_score']
# voice = user_data['voice_score']
# screen = user_data['screen_score']

# # Calculate burnout score
# burnout_score = round(typing * 0.3 + voice * 0.4 + screen * 0.3, 2)

#     #Defining weights
# weights = {"Typing": 0.3,
#             "Voice": 0.4, 
#             "Screen": 0.3}
    
#     #Calculated weighted contributions(SHAP-style)
# contributions = {
#         "Typing": weights["Typing"] * typing,
#         "Voice": weights["Voice"] * voice,
#         "Screen": weights["Screen"] * screen
#     }

#     fig = go.Figure(go.Bar(
#         x=list(contributions.keys()),
#         y=list(contributions.values()),
#         # orientation='h',
#         marker_color=['#bfb3de', '#a592d8', '#8a6cd4'],
#          text=[
#         f"Modality: {modality} | Contribution: {score:.2f}"
#         for modality, score in contributions.items()
#     ],
#         textposition="outside"
#     ))

#     fig.update_layout(
#         height=450,
#         xaxis_title="Modality",
#         yaxis_title="Contribution Score",
#         margin=dict(l=30, r=40, t=30, b=30),
#         template="simple_white"
#     )

#     st.plotly_chart(fig, use_container_width=True)