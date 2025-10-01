import os 
os.system("cls")

#Crie um programa que leia 4 notas,armazenando em um vetor e calcule media aritmetica
lista_nota = []

for i in range(4):
    nota = int(input(f"Digite as suas {i + 1}ª notas: "))
    lista_nota.append(nota)

media = sum(lista_nota) / 4

#Resultados
print("\n-------Resultados------")
if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")
print(f"Media aritmetica {media}")