import os
os.system("cls")

nota = int(input("Qual foi sua nota? "))

if nota < 5 or nota > 10:
    print("Nota invalida.")
else:
    print(f"NOTA: {nota}")