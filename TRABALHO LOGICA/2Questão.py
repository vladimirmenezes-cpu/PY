import os
os.system("cls")

nome = input("Digite seu nome:")
print()
sexo = input("Digite seu sexo (F para feminino, M para masculino): ")
print()
civil = input("Digite seu estado civil:")

if sexo == 'F' and civil == 'casada':

    tempo = input("Quantos anos de casada?")

    print("\n--- DADOS DO USUÁRIO ---")
    print(f"Nome: {nome}")
    print(f"Sexo: {sexo}")
    print(f"Estado Civil: {civil}")
    print(f"Tempo de casada: {tempo} anos.")

else:

    print("\n--- DADOS DO USUÁRIO ---")
    print(f"Nome: {nome}")
    print(f"Sexo: {sexo}")
    print(f"Estado Civil: {civil}")

