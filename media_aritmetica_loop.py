import os
os.system("cls")

soma = 0
quantidade = 0

while True:
    notas = float(input("Digite a nota do aluno:"))
    soma += notas
    quantidade += 1
    continuar = input("Deseja continuar? (S/N)").upper()
    if continuar == "N":
        break

media = soma / quantidade
print(f"A média das notas é: {media:.2f}")
print(f"Foram digitadas {quantidade} notas.")
