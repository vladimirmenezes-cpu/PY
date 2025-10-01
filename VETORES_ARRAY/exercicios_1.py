import os 
os.system("cls")

#crie um programa que leis 3 notas, armazenando em um vetor e calcule a media aritmetica
#depois mostre as notas e a media aritmetica

lista_nota = []

for i in range(3):
    nota = int(input(f"Digite as suas {i + 1}ª notas: "))
    lista_nota.append(nota)

media = sum(lista_nota) / 3

for i in range(3):
    print(f"\nNotas: {lista_nota[i]}")

print(f"Media aritmetica {media}")