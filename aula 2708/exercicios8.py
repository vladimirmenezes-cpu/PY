import os
os.system("cls")

numero1 = int(input("Informe a quantidade de maçãs: "))


if numero1 <= 12:
    preco_unitario = 1.30
else:
     preco_unitario = 1.00

valor_total = numero1 * preco_unitario

print(f"Preço total: {valor_total: .2f}")
print(f"preço por maça {preco_unitario}")


