import streamlit as st

st.title("Mi primera aplicación en python")

st.sidebar.title("Parametros")

st.write("Elaborado por: Jazmin Huillca")

sesion = st.selectbox("Seleccione una sesión"),["Sesion 1","Sesion 2", "Sesion 3", "Sesion 4"])


