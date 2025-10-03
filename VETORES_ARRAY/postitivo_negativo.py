import os 
os.system("cls")


netagivo = 0
positivo = 0 
soma_positivo = 0

lista = []

for i in range(5):
    numero = int(input(f"{i + 1}- Digite 5 numeros Positivo e Negativo: "))
    lista.append(numero)
    if numero > 0:
        positivo += 1
        soma_positivo += numero
    elif numero < 0:
        netagivo += 1

print("===== RESULTTADO====")
print(f"Numero Positivo: {positivo}")
print(f"Soma dos numeros Positivos: {soma_positivo}")
print(f"Numeros Negativos: {netagivo}")