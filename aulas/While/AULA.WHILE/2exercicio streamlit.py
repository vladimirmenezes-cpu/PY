import streamlit as st

st.title("Laço de repetição")

st.write("Crie um programa que solicite ao usuario seu login e uma senha" \
"  o programa deve cotninuar pedindo o login e a senha ate que ambos estejam corretos")


login_cadastrado = "vlad"
senha_cadastrada = "123456"

login_informado = st.text_input("Digite seu login: ")
senha_informada = st.text_input("Digite sua senha: ", type="password")


if st.button("Acessar"):
    if login_informado == login_cadastrado and senha_informada == senha_cadastrada:
            st.success("Acesso liberado")
    
    else:
            st.info("Acesso negado")