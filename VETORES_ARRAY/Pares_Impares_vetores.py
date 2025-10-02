import os 
os.system("cls")

#Crie um programa que leia 4 notas,armazenando em um vetor e calcule media aritmetica
lista_nota = []
pares = 0
impares = 0

for i in range(6):
    nota = int(input(f"{i + 1} - Digite 6 numeros para saber qual é par e impar: "))
    lista_nota.append(nota)
    if lista_nota[i] % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"\n-------Resultado-------")
print(f"\nNumeros informados: {lista_nota}")
print(f"\nPares: {pares}")
print(f"\nimpares: {impares}")