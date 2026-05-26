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

  precio = st.number_input("Ingrese el precio del producto")
  descuento = st.number_input("Ingrese el descuento del producto")

precio_final_producto = precio - (precio*descuento)

elif sesion == "Sesión 3":
  st.write("Bienvenido a la sesión 3")
  inicio_rango = st.slider("seleccione un valor",min_value = 0, max_value=20, value =7)
