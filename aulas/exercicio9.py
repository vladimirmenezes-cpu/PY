import os
os.system("cls")

numero1 = float(input("Nota primeiro semestre: "))
numero2 = float(input("Nota segundo semestre: "))

media = (numero1 + numero2)/ 2 



if media >= 9:
    conceito = "A"
    resultado = "APROVADO"
elif media >= 7.5:
    conceito = "B"
elif media >= 4:
    conceito = "D"
else:
    conceito = "E"

if media > 6:
    resultado = "APROVADO"
else:
    resultado = "REPROVADO"

print(f"\nMÉDIA: {media}")
print(f"Conceito: {conceito}")
print(f"Resultado: {resultado}")