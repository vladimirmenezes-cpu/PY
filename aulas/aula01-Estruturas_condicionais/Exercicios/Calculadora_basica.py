import os
os.system("cls")

#Faça um algoritmo que solitice ao usuário dois números e um caractere que calcula as operações basicas
#(+-*/)
#Mostre os numeros informados pelo usuario, o operador escolhido e o resultado.

numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite um numero: "))
operacao = input("Digite a operação desejada ( + , - , * ou /): ")




match operacao:
    case '+':
        resultado = numero1 + numero2
    case '-':
        resultado = numero1 - numero2
    case '*':
        resultado = numero1 * numero2
    case'/':
        resultado = numero1 / numero2
    
print(f"Numeros informados: {numero1} {operacao} {numero2}")
print(f"resultado: {resultado}")
print("FIM")