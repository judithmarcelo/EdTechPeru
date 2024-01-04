import streamlit as st

st.header('Ejercicios Economía I')

st.subheader('Ejercicio 2')
st.write('Se ha estimados las siguientes funciones para el mercado de hoteles:') 
st.latex('Demanda: Q^d=7000-2P') #7000 va a ser variable
st.latex('Oferta: Q^o=3000+6P')
st.write('Donde Q es el número de habitaciones, y P el precio en soles de cada habitación.')
st.write('a) Indique el precio y la cantidad de equilibrio en el mercado.')
number = st.number_input ('Precio en soles de cada habitación', value = None, placeholder='Escribe tu respuesta')

Revisar_Respuetas = st.button('Revisar respuestas')

if number == 500:
    st.write('muy bien')
else:
    st.write ('mal')

with st.expander('Solucionario_Ejercicio2'):
    st.write('El equilibrio surge cuando la cantidad demanda y la cantidad ofertada son iguales; así, se iguala las cantidades:')
    st.latex('Q^d = Q^o ')
    st.latex('7000-2P = 3000 + 6P')
    st.latex('4000 = 8P')
    st.latex('P=500')


