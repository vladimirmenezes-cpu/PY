import streamlit as st
import time 
st.title("Laço de reptição - For")
st.header("CONTAGEM")

numero = st.number_input("DIGITE ATE ONDE VOCE QUE O LAÇO.", step = 1)

if st.button("INICIAR"):
    for i in range(100,121, 2):
        st.info(i)
        time.sleep(1)
    st.header("FIM")
            