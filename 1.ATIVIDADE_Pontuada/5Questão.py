import os
os.system("cls")

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo  valor: "))
operacao = input("Digite a operação (+, -, *, /): ")

resultado = 0

match operacao:
    case '+':
        resultado = a + b
    case '-':
        resultado = a - b
    case '*':
        resultado = a * b
    case '/':
        resultado = a / b
    case _:
        print("Invalido!")

print(f"Resultado: {a} {operacao} {b} = {resultado: }")
