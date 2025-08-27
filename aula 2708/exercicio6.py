import os
os.system("cls")

numero1 = int(input("Informe sua idade: "))

if numero1 <= 15: 
    print("Não pode votar")
elif 16 >= numero1 >= 17:
    print("Voto opcional")
elif 18 <= numero1 <= 64:
    print("Votos obrigatorios")
elif numero1 > 65:
    print("VOTO Não OBRIGATORIO")