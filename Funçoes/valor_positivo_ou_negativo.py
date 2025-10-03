import os
os.system("cls")

# Função com passagem de parametros
def teste(numero):
    if numero > 0:
        print("O numero é Positivo")
    else:
        print("Numero é Megativo")


numero = int(input("Digite um numnero: "))
os.system("cls")
teste(numero)