import streamlit as st
import time 
st.title("Laço de reptição - For")
st.header("SOMA DE 5 NUMEROS")

soma = 0

for i in range(1,6):
        numero =st.number_input(f"Digite o {i}º numero para a soma.", step = 1, min_value=0) 
        soma = soma + numero

if st.button("INICIAR"):
    st.success(f"A soma dos 5 numeros é {soma}")
else:
    st.info("Clique em INICIAR para ver o resultado")

