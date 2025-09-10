import streamlit as st

st.title("BLITZZZZZZZZZZ")

idade = st.number_input("Digite sua idade,Melianteeee!!!!")

if  st.button("Verificar"):
    if idade < 18:
        st.write("MENOR DE IDADE,VAGABUNDOO")
    else:
            st.write("MAIOR DE IDADE,VAI APANHARR!00")

else:
     st.warning("FALE SUA IDADE,VAGABUNDO")