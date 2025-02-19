import pandas as pd
import plotly.express as px
import streamlit as st
car_data = pd.read_csv('vehicles_us.csv')
st.header("análisis exploratorio de datos vehículos US")
if st.button("Generar Histograma del Odometro"):
    st.write("Histograma del Odometro:")
    fig_hist = px.histogram(car_data, x='odometer', title='Distribución del Odometro')
    st.plotly_chart(fig_hist,use_container_width=True)
    
if st.button('Generar Gráfico de Dispersión del Odometro'):
    st.write("Gráfico de Dispersión del Odometro:")
    fig_dispersion = px.scatter(car_data, x='odometer', y='price', title='Gráfico de Dispersión: Odometro vs Precio')
    st.plotly_chart(fig_dispersion)

st.subheader("Selecciona el tipo de gráfico que deseas ver")

histograma = st.checkbox("Mostrar Histograma por tipo de vehiculo")

if histograma :
    fig_hist_type = px.histogram(car_data, x='type', y='odometer', histfunc='sum', title="Histograma por Tipo de Vehículo")
    st.plotly_chart(fig_hist_type)


dispersion = st.checkbox("Mostrar Gráfico de Dispersión por tipo de vehiculo")

if dispersion:
    fig_scatter_type = px.scatter(car_data, x='odometer', y='price', color='type', title="Dispersión: Odometro vs Precio por Tipo")
    st.plotly_chart(fig_scatter_type)
