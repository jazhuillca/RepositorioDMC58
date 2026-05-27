import streamlit as st
import numpy as np

st.title("Mi primera aplicación en python")

st.sidebar.title("Parametros")

st.write("Elaborado por: Jazmin Huillca")

st.sidebar.image("DMC.png")

add_selectbox = st.sidebar.selectbox(
  "How would you like to be contacted?",
  ("Email", "Home phone", "Mobile phone")
)

sesion = st.sidebar.selectbox("Seleccione una sesión",["Sesión 1","Sesión 2", "Sesión 3", "Sesión 4"])

if sesion == "Sesión 1":
  st.write("Bienvenido a la Sesión 1")
  st.image("python_logo.png")

elif sesion == "Sesión 2":
  st.write("Bienvenido a la Sesión 2")

  precio = st.number_input("Ingrese el precio del producto", min_value = 0 , max_value = 5000 , value =1200)

  elif sesion == "Sesión 3":

  st.write("Bienvenido la sesión 3")

  fin_rango = st.slider("Selecione un valor",min_value = 0 , max_value=20, value =7 )

  arreglo = np.arange(0 , fin_rango)

  st.write(arreglo)

else:

  st.write("Bienvenido la sesión 4")
elif sesion == "Sesión 3":
  st.write("Bienvenido a la Sesión 3")
  inicio_rango = st.slider("seleccione un valor",min_value = 0, max_value=20, value =7)
