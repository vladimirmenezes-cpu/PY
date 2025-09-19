import os
os.system("cls")

#Construa um algoritmo que calcule a media artimética de várias valores inteiros positiovos.
# O final da leitura acontecera quando for lido um valor negativo.

soma = 0
quantidade = 0

while True:
    valor = int(input("Digite um valor inteiro positivo: "))
    if valor < 0:
        break
    soma += valor
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"A média dos valores é: {media:.2f}")
else:
    print("Nenhum valor válido foi digitado.")