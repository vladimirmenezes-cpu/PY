import os
os.system("cls")


altura = float(input("Digite sua altura em metros (ex: 1.75): "))
sexo = input("Digite seu sexo (M para Masculino, F para Feminino): ")

match sexo:
  case "M":
    peso_ideal = (72.7 * altura) - 58
    print(f"\nSeu peso ideal é: {peso_ideal:} kg")
  case "F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"\nSeu peso ideal é: {peso_ideal:} kg")
  case _:
    print("\nOpção de sexo inválida. Por favor, execute novamente e insira 'M' ou 'F'.")