import streamlit as st
import time 
st.title("Laço de reptição - For")
st.header("CONTAGEM Regressiva")

numero = st.number_input("Digite o numero para a contagem regressiva.", step = 1)

if st.button("INICIAR"):
    for i in range(numero, 0, -1):
        st.warning(i)
        time.sleep(1)
        st.snow()
    st.success("FIM")