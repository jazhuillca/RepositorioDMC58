import streamlit as st
import pandas as pd
import numpy as np
import librerias_funciones as lf

st.title("Mi primera aplicación en python")

st.sidebar.title("Parametros")

st.write("Elaborado por: Jazmin Huillca")

st.sidebar.image("DMC.png")

sesion = st.sidebar.selectbox("Seleccione una sesión",["Sesión 1","Sesión 2", "Sesión 3", "Sesión 4"])

if sesion == "Sesión 1":
  st.write("Bienvenido a la Sesión 1")
  st.image("python_logo.png")

elif sesion == "Sesión 2":
  st.write("Bienvenido a la Sesión 2")

  precio = st.number_input("Ingrese el precio del producto", min_value = 0 , max_value = 5000 , value =1200)
  descuento = st.number_input("Ingrese el descuento del producto del 0 al 100%", min_value = 0 , max_value = 100)

  precio_final_producto = precio - (precio*(descuento/100))
  st.write("El precio final del producto es: ", precio_final_producto)

elif sesion == "Sesión 3":
  st.write("Bienvenido a la Sesión 3")
  inicio_rango = st.slider("seleccione un valor",min_value = 0, max_value=20, value =7)
