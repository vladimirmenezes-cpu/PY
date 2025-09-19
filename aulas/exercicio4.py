import os
os.system("cls")

numero1 = int(input("Informe a nota: "))
numero2 = int(input("Informe a nota: " ))

soma = numero1+numero2
media = (numero2+numero1)/ 2
produto = numero1*numero2

if numero1 < numero2:
    print ("Segundo numero é maior")
else:
    print("Primeiro numero é maior")

if numero1 == numero2:
    print ("Os numeros são iguais!!")

print(f"Média: {media}\nSoma: {soma}\nProduto: {produto}")


