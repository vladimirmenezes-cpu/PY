import os
os.system("cls")

numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite um numero: "))
operação = input("Digite a operação desejada ( + , - , * ou /)")




match operação:
    case operação == '+'
        resultado = numero1 + numero2
    case operação == '-'
        resultado = numero1 - numero2
    case operação == '*'
        resultado = numero1 * numero2
    case operação == '/'
        resultado = numero1 / numero2
    
print(f"Numeros informados: {numero1} {operação} {numero2}")
print(f"resultado: {resultado}")
print("FIM")