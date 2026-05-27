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

sesion = st.sidebar.selectbox(
    "Seleccione una sesión",
    ["Sesión 1", "Sesión 2", "Sesión 3", "Sesión 4"]
)

# Función definida directamente (reemplaza lf.cuota_prestamo)
def cuota_prestamo(principal, tasa_anual, anios, pagos_anio):
    tasa_periodo = tasa_anual / pagos_anio
    n = anios * pagos_anio
    if tasa_periodo == 0:
        return principal / n
    cuota = principal * tasa_periodo / (1 - (1 + tasa_periodo) ** -n)
    return cuota

if sesion == "Sesión 1":
    st.write("Bienvenido a la Sesión 1")
    st.image("python_logo.png")

elif sesion == "Sesión 2":
    st.write("Bienvenido a la Sesión 2")
    precio = st.number_input(
        "Ingrese el precio del producto",
        min_value=0, max_value=5000, value=1200
    )

elif sesion == "Sesión 3":
    st.write("Bienvenido a la Sesión 3")
    fin_rango = st.slider(
        "Seleccione un valor",
        min_value=0, max_value=20, value=7
    )
    arreglo = np.arange(0, fin_rango)
    st.write(arreglo)

else:  # Sesión 4
    st.write("Bienvenido a la Sesión 4")
    principal = st.number_input("Ingrese el monto del préstamo", value=1000)
    tasa_anual = st.number_input(
        "Ingrese la tasa anual en decimal",
        value=0.1, min_value=0.0, max_value=1.0
    )
    anios = st.number_input("Ingrese el número de años del préstamo", value=1)
    pagos_anio = st.number_input(
        "Ingrese la cantidad de pagos por año", value=12
    )
    cuota = round(cuota_prestamo(principal, tasa_anual, anios, pagos_anio), 2)
    st.write(f"El valor de la cuota es {cuota}")
