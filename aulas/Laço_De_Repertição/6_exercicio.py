import streamlit as st

st.title("VERIFICANDO MEDIA")

nota1 = st.number_input("DIGITE SUA NOTAAAA!!!!")
nota2 = st.number_input("DIGITE SUA NOTAAAA!!!!,")

soma = nota1 + nota2
media = (nota2 + nota1) / 2
produto = nota1 * nota2
menor_valor = min(nota1, nota2)
maior_valor = max(nota1, nota2)

if st.button("Verificar"):
    st.write(f"A soma dos dois números é: {soma}")
    st.write(f"A Mediaa dos dois números é: {media}")
    st.write(f"A Multiplicação dos dois números é: {produto}")
    st.write(f"A Menor nota  dos dois números é: {menor_valor}")
    st.write(f"A maior nota dos dois números é: {maior_valor}")
else:
    st.info("Informe os numeros.")



# sucesse - verde
# warting - amarelo
# info - azul
# error - vermelho 