import streamlit as st
import time 
st.title("Laço de reptição - For")
st.header("CONTAGEM")


if st.button("INICIAR"):
    for i in range(1,20, 2):
        st.info(i)
        time.sleep(1)
    st.header("FIM")
            