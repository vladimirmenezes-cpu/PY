import os
os.system("cls")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6.0:
    print("APROVADO! PARABENS")
elif media >= 4.1:
    print("EM RECUPERAÇÃO!")
else:
    print("REPROVADO!")

