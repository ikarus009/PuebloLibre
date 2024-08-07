import streamlit as st
from pages import serenazgo_platform, citizen_app, sereno_app

st.set_page_config(page_title="Sistema de Emergencia Pueblo Libre", layout="wide")

st.sidebar.title("Navegación")
page = st.sidebar.radio("Ir a", ["Plataforma de Serenazgo", "App del Ciudadano", "App del Sereno"])

if page == "Plataforma de Serenazgo":
    serenazgo_platform.show()
elif page == "App del Ciudadano":
    citizen_app.show()
elif page == "App del Sereno":
    sereno_app.show()