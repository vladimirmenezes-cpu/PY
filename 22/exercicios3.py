import os
os.system("cls")

numero1 = float(input("Informe a primeira nota do 3 semestre: " ))
numero2 = float(input("Informe a segunda nota do 3 semestre: " ))
numero3 = float(input("Informe a terceira nota do 3 semestre: " ))

media = (numero1+numero2+numero3)/3

if media >= 6.9:
    print ("REPROVADO!")
else:
    print("APROVADO!")