import os
os.system("cls")

#Elabore um algoritmo para resolver a seguinte questão:
#Escreva um programa que solicite ao usuário a quantidade de maçãs desejadas.
#As maçãs custarão R$1,30 cada, se forem compradas menos de uma duzia, e custarão R$ 1,00 cada, se forem compradas pelo menos 12
#Calcule e mostre valor total da compra.

numero1 = int(input("Informe a quantidade de maçãs: "))

if numero1 <= 12:
    preco_unitario = 1.30
else:
     preco_unitario = 1.00

valor_total = numero1 * preco_unitario

print(f"\nPreço total: {valor_total: .2f}")
print(f"\npreço por maça {preco_unitario}")


