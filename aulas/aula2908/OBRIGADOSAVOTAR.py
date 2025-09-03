import os
os.system("cls")

idade = int(input("Digite sua idade: "))

voto_obrigatorio = idade >= 18 and idade <= 65


if voto_obrigatorio:
    print("ELEITOR É OBRIGADO A VOTAR.")
else:
    print("O ELEITOR NÃO É OBRIGADO A VOTAR")