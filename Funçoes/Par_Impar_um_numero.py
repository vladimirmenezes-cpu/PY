import os
os.system("cls")

# Função com passagem de parametros
def teste(numero):
    print(f"O numero é: {numero}")
    if numero % 2 == 0:
        print("O numero é PAR")
    else:
        print("Numero impar")


numero = int(input("Digite um numnero: "))
os.system("cls")
teste(numero)