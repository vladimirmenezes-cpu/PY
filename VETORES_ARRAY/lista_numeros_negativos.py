import os 
os.system("cls")


netagivo = 0
positivo = 0 
soma_positivo = 0

lista = []

for i in range(5):
    numero = int(input(f"{i + 1}- Digite 5 numeros: "))
    if numero < 0:
            numero = 0
    lista.append(numero)


print(f"Lista: {lista}")