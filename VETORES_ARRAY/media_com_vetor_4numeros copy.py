import os 
os.system("cls")

#Crie um programa que leia 4 notas,armazenando em um vetor e calcule media aritmetica
lista_nota = []


for i in range(5):
    nota = int(input(f"Digite as suas {i + 1}ª notas: "))
    lista_nota.append(nota)

maior_nota = max(lista_nota)
menor_nota = min(lista_nota)
#Resultados
print("\n-------Resultados------")
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")