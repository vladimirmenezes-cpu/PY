import os
os.system("cls")

print("Laço de repetição - While")

soma = 0
quantidade = 2

for i in range(quantidade):
    while True:
        numero = int(input("dIGITE UM NUMERO: "))
        if numero >= 0 and numero <= 10:
            break
    soma = soma + numero

media = soma / quantidade


print(f"Nota {media}")  