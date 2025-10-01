import os 
os.system("cls")

# Criando um vetor (Lisa)
lista_notas = []

# Inserindo notas.
for i in range(3):
    nota = int(input(f"Digite a {i+1}ª nota:"))
    lista_notas.append(nota)

# Soma += nota
soma = sum(lista_notas)

for i in range(3):
    print(f"Nota: {lista_notas[i]}")

print(f"Soma: {soma}")
print(f"Soma: {soma}")
#
print("FIM")
