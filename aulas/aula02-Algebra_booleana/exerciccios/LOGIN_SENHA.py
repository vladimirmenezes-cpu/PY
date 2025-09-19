import os
os.system("cls")

#Elabore um algoritmo para soliticar ao usuario o login e senha
#considere que os dados do usuario ja estão cadastrados.
#caso o login estejam corretos,mostre a mensagem:
#BEM-VINDO!
#Caso contrario, mostre a mensagem:
#"Login ou senha invalidos."

login_cadastrado = "usuario123"
senha_cadastrada = "12345678"

login_informado = input("INFORME SEU LOGIN: ")
senha_informado = input("INFORME SUA SENHA: ")

if login_informado == login_cadastrado and senha_informado == senha_cadastrada:
    print("SEJA BEM VINDO!!")
else:
    print("SENHA OU LOGIN INVALIDOS")