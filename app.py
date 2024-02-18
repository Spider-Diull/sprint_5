import streamlit
import pandas
import plotly_express

car_data=pandas.read_csv('vehicles_us.csv') # Leimos los datos del CSV
hist_button = streamlit.button('Construir histograma') # crear un botón
#BOTON PARA CONSTRUIR HISTOGRAMA
if hist_button: # al hacer clic en el botón
    streamlit.write('Creación de un histograma para el conjunto de datos de anuncios de venta de vehiculos')# escribir un mensaje
    hist_graphic = plotly_express.histogram(car_data, x="odometer")# crear un histograma
    streamlit.plotly_chart(hist_graphic, use_container_width=True)# mostrar un gráfico Plotly interactivo
    
#BOTON PARA CONSTRUIR GRAFICO DE DISPERSION
scatter_chekbox = streamlit.checkbox('Costruir grafico de dispersion') # crear una casilla de verificación
if scatter_chekbox:
    streamlit.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de vehiculos')# escribir mensaje
    scatter_graphic=plotly_express.scatter(car_data,x='odometer',y='price')# crear grafico de dispersion
    streamlit.plotly_chart(scatter_graphic,use_container_width=True)# mostrar un gráfico Plotly interactivo
