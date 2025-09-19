import os
os.system("cls")


numero = int(input("Digite um número para ver a sua tabuada: "))

print(f"\n--- Tabuada do {numero} ---")

for i in range(1, 500):
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")

