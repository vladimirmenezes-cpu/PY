import os
os.system("cls")

#O algoritmo deve soliticas ao usuário o nome do aluno, duas notas.
#Calcule a média e mostre o conceito correspondente:
#A mensagem 'Aprovada' se o conceito for A,B ou C
#A mensagem 'Reprovado' se o conceito for D ou E.


nome = input("Digite o nome do aluno: ")
numero1 = float(input("Nota primeiro semestre: "))
numero2 = float(input("Nota segundo semestre: "))

media = (numero1 + numero2)/ 2 

if media >= 9:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
else:
    conceito = "E"

if conceito in ["A", "B", "C"]:  
    resultado = "Aprovado"
else:
    resultado = "Reprovado"


print(f"\nAluno: {nome}")
print(f"\nMÉDIA: {media}")
print(f"Conceito: {conceito}")
print(f"Resultado: {resultado}")