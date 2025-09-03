import os
os.system("cls")

nota = float(input("Qual foi sua nota? "))

if nota >= 0 and nota <= 10:
    print(f"NOTA: {nota}")
else:
    print("NOTA invalida.")