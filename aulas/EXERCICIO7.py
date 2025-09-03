import os
os.system("cls")

numero1 = int(input("Informe sua idade: "))

if numero1 < 16: 
    print("Não pode votar")
elif numero1 <= 18:
    print("Voto opcional")
elif 18 <= numero1 <= 64:
    print("Votos obrigatorios")
elif numero1 >= 65:
    print("VOTOS NÃO OBRIGATORIOS")