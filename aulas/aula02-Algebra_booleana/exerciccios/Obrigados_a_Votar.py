import os
os.system("cls")

#Elabore um algoritmo usado operações logicas para informar se uma pessoa é obrigada a votar.
#Considere que a regra é que menores de 18 e maiores que 65 não são obrigados a votar.

idade = int(input("Digite sua idade: "))

voto_obrigatorio = idade >= 18 and idade <= 65


if voto_obrigatorio:
    print("ELEITOR É OBRIGADO A VOTAR.")
else:
    print("O ELEITOR NÃO É OBRIGADO A VOTAR")