import streamlit as st
import time 
st.title("Laço de reptição - For")
st.header("MULTIPLICAÇÃO")

numero = st.number_input("Digite o numero para a multiplicação.", step = 1)

if st.button("INICIAR"):
    for i in range(1,150):
        mult = numero * i
        st.write(f"{numero} * {i} = {mult}")
        st.info(mult)
        time.sleep(1)
    st.success("FIM")
            