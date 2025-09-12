import streamlit as st
import time 
st.title("Laço de reptição - For")
st.header("MEDIA DE 3 NOTAS")

media = 0
soma = 0
for i in range(1,4):
    numero = st.number_input(f"Digite a sua nota {i}:", step=1)
    soma = soma + numero 
    media = soma  / 3
    st.balloons()

if st.button("Verificar"):
    if media >= 7:
        st.success(f" APROVADO! Parabens sua media foi {media}")
    elif media >= 4:
        st.warning(f"RECU RECU : {media}")
    else:
        st.error("REPROVADO BURRAO TU")
    st.success(f"Sua media é: {media}")
    
    