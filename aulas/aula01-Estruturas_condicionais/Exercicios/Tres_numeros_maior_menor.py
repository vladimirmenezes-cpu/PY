import os
os.system("cls")

#Elabore um algoritmo usadno operações lógicas para ler números e escrever:

#Os 3 números informados.
#O maior número;
#O menor número;


numero1 = int(input("Informe a nota: "))
numero2 = int(input("Informe a nota: " ))
numero3 = int(input("Informe a nota: " ))


print(f"\nOs números informados foram: {numero1}, {numero2} e {numero3}")
print(f"O maior número é: {max(numero1,numero2,numero3)}")
print(f"O menor número é: {min(numero1,numero2,numero3)}")