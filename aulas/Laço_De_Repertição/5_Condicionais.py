import streamlit as st

st.title("BLITZZZZZZZZZZ")

nota = st.number_input("DIGITE SUA NOTAAAA!!!!")

if  st.button("Verificar"):
    if nota < 7:
        st.error("REPROVADO,BURRO")
    else:
            st.success("aprovadoo!! bom garoto")

else:
     st.warning("FALE SUA NOTA,ESTUDANTE")




# sucesse - verde
# warting - amarelo
# info - azul
# error - vermelho 