import streamlit as st
import time 
st.title("Laço de reptição - For")
st.header("MEDIA DE 4 NOTAS")

media = 0
soma = 0
for i in range(1,5):
    numero = st.number_input(f"Digite a sua nota {i}:", step=1)
    soma = soma + numero 
    media = soma  / 4
    st.balloons()

if st.button("Verificar"):
    st.success(f"Sua media é: {media}")
    