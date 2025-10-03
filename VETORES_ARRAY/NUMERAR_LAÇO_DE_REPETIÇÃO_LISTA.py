import os 
os.system("cls")

lista = []

for i in range(5):
    numero = int(input(f"{i + 1}- Digite 5 numeros: "))
    if numero < 0:
            numero = 0
    lista.append(numero)

print("\nExibindo numeros")
for i, numero in enumerate(list, start=1):
        print(f"{i}° numero: {numero}")