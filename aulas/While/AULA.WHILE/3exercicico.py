import os 
os.system("cls")

login_cadastrado = "vlad"
senha_cadastrada = "123456"
tentativas = 0


while True: 

    login_informado = input("Informe seu login:")
    senha_informada = input("Informe senha: ")

    if login_informado == login_cadastrado and senha_informada == senha_cadastrada:
        print("Acesso liberado")
        break
    else:
        tentativas += 1   
        print("Acesso negado")
        if tentativas == 3:
            print("Numero maximo de tentativa, aguarde um periodo")
            break