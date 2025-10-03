import os
os.system("cls")

# Função com passagem de parametros
def teste(numero):
    for i in range(1, 11):
        print(f"{numero} X {i} = {numero * i}")  


numero = int(input("Digite um numnero: "))
os.system("cls")
teste(numero)