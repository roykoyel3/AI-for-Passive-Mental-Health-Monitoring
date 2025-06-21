import streamlit as st 

def get_gui():
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
