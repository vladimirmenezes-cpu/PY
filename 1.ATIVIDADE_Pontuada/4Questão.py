import os
os.system("cls")

morango = float(input("Digite a quantidade de morangos (em Kg): "))
maca = float(input("Digite a quantidade de maçãs (em Kg): "))


preco_morango = 0 
preco_maca = 0 

if morango <= 5:
    preco_morango = morango * 2.50
else:
    preco_morango = morango * 2.20

if maca <= 5:
    preco_maca = maca * 1.80
else:
    preco_maca = maca * 1.50

preco = preco_morango + preco_maca
peso = morango + maca

if peso >= 10 or preco > 15.00:
    desconto = preco * 0.10
    valor_a_pagar = preco - desconto
print(f"O valor total a ser pago é: R$ {valor_a_pagar:.2f}")
