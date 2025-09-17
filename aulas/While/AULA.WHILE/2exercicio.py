import os 
os.system("cls")

login_cadastrado = "vlad"
senha_cadastrada = "123456"



while True: 

    login_informado = input("Informe seu login:")
    senha_informada = input("Informe senha: ")

    if login_informado == login_cadastrado and senha_informada == senha_cadastrada:
        print("Acesso liberado")

    else:   
        print("Acesso negado")