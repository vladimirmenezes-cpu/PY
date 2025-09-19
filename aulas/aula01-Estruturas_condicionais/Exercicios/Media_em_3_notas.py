import os
os.system("cls")

#Elabore um algoritmo para soliticar ao usuário três notas.
#Calcule a média do aluno.
#Caso a média do aluno seja menor que 7, o aluno está reprovado.
#Mostrar:media e se está aprovado ou reprovado

numero1 = float(input("Informe a primeira nota do 3 semestre: " ))
numero2 = float(input("Informe a segunda nota do 3 semestre: " ))
numero3 = float(input("Informe a terceira nota do 3 semestre: " ))

media = (numero1+numero2+numero3)/3

if media < 7:
    print ("REPROVADO!")
else:
    print("APROVADO!")