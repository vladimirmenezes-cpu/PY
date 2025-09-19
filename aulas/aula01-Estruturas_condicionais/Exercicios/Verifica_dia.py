import os
os.system("cls")

#Desenvolva um programa que receba como entrada um numero inteiro que represente um dos 7 dias da semana
# e imprima se esse dia é util,final de semana ou invalido.
#Considere que domingo é o dia 1 e Sabado o dia 7

dia = int(input("Digite um numero para o dia da semana: "))

match dia:
    case 1:
        print("Domingo - Final de semana")
    case 2:
        print("Segunda-feira - Dia útil")
    case 3:
        print("Terça-feira - Dia útil")
    case 4:
        print("Quarta-feira - Dia útil")
    case 5:
        print("Quinta-feira - Dia útil")
    case 6:
        ("Sexta-feira - Dia útil")
    case 7:
        print("Sabado - Final de semana")
    case _:
        print("Opção invalida.")

print("FIM")