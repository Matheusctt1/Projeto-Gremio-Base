# Definições da pagina de rosto

import streamlit as st

def exibirPagina():
    st.title("CDD BASE")
    st.markdown(
            """
            <style>
            .st-emotion-cache-12fmjuu{
                background: transparent;
            }

            .st-emotion-cache-asc41u e1nzilvr2, .st-emotion-cache-ai8gcz, .st-emotion-cache-1nj1hs9{
                color: black;
            }
            .stApp {
                
                background-image: url("https://i.pinimg.com/originals/dd/cd/57/ddcd57f6b2f53b01128250b390d9b974.png");
                background-size: 1600px, 726px;
                background-repeat: no-repeat;
                background-position: center;
            }
            </style>
            """,
            unsafe_allow_html=True
        )