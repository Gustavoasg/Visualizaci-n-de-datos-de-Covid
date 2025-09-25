import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("COVID-19 Data Visualization 📊")

st.write("Este dashboard muestra datos de COVID-19 usando Streamlit.")

# Ejemplo de gráfico vacío
df = pd.DataFrame({"x": [1,2,3], "y": [10,20,30]})
st.line_chart(df.set_index("x"))
