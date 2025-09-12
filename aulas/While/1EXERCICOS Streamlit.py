import streamlit as st

st.title("Laço de repetição - While")

numero = st.number_input("Digite uma nota", step=1)

if st.button("Verificar"):
             if numero < 0 or numero > 10:
                     st.warning("A nota deve ser entre 0 e 10")
             else:
                st.info(f"Nota: {numero}")