import os
os.system("cls")

print("Laço de repetição - While")

while True:
    numero = int(input("dIGITE UM NUMERO: "))
    if numero >= 0 and numero <= 10:
        break

print(f"Nota {numero}")  