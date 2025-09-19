import streamlit as st
import time 
st.title("Laço de reptição - For")
st.header("CONTAGEM DE 1 A 10.")

numero = st.number_input("DIGITE ATE ONDE VOCE QUE O LAÇO.", step = 2)

if st.button("INICIAR"):
    for i in range(1,numero+1):
        st.info(i)
        time.sleep(1)
    st.header("FIM")
            