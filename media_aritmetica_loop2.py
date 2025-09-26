import os 
os.system("cls")

soma = 0
quantidade = 0

while True:
    nota = float(input("Digite a nota do aluno:"))
    contador += 1
    soma =+ nota

    continuar = input("Deseja continuar? Digite S ou N:").lower()
    if continuar == "n":
        break

    media = soma / quantidade
print(f"A média das notas é: {media:.2f}")
print(f"Foram digitadas {quantidade} notas.")