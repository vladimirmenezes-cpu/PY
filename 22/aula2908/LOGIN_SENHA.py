import os
os.system("cls")

login_cadastrado = "usuario123"
senha_cadastrada = "12345678"

login_informado = input("INFORME SEU LOGIN: ")
senha_informado = input("INFORME SUA SENHA: ")

if login_informado == login_cadastrado and senha_informado == senha_cadastrada:
    print("SEJA BEM VINDO!!")
else:
    print("SENHA OU LOGIN INVALIDOS")