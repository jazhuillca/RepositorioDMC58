import streamlit as st

st.title("Mi primera aplicación en python")

st.sidebar.title("Parametros")

st.write("Elaborado por: Jazmin Huillca")

st.sidebar.image("DMC.png")

sesion = st.sidebar.selectbox("Seleccione una sesión",["Sesion 1","Sesion 2", "Sesion 3", "Sesion 4"])

if sesion == "Sesión 1":
  st.write("Bienvenido a la sesión 1")
  st.image("Python_logo.png")

elif sesion == "Sesión 2":
  st.write("Bienvenido a la sesión 2")

elif sesion == "Sesión 3":
  st.write("Bienvenido a la sesión 3")
