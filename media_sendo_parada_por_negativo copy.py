import os
os.system("cls")

# Faça um algoritmo que leia uma quantidade não determinada de numeros inteiros positivos.
# A = quantiade numeros pares e impares
# B = media de valores pares
# C = media geraal dos numeros lidos

soma = 0
quantidade = 0
pares = 0
impares = 0
soma_pares = 0

while True:
        valor = int(input("Digite um número inteiro positivo (negativo para encerrar): "))
        if valor == 0:
            break
        soma += valor
        quantidade += 1
        if valor % 2 == 0:
            pares += 1
            soma_pares += valor
        else:
            impares += 1

if quantidade > 0:
    media_geral = soma / quantidade
    if pares > 0:
        media_pares = soma_pares / pares
    else:
        media_pares = 0
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")
    print(f"Média dos valores pares: {media_pares:.2f}")
    print(f"Média geral dos números lidos: {media_geral:.2f}")
else:
    print("Nenhum valor positivo foi digitado.")