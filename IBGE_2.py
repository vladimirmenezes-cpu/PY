import os
os.system("cls")

total_familia = 0
soma_salario = 0
soma_filhos = 0
menor_salario = 0
maior_salario = 0

while True:
    print(""" Menu:
    1. Adicionar FAMILIA
    2. Exibir relatório
    """)
    escolha = input("Escolha uma opção: ")

    match escolha:
        case "1":
            salario = float(input("Salário: "))
            numero_filhos = int(input("Número de filhos: "))
            
            total_familia += 1
            soma_salario += salario
            soma_filhos += numero_filhos

            if salario > maior_salario:
                maior_salario = salario
            if menor_salario < menor_salario:
                menor_salario = salario

        case "2":
            if total_familia == 0:
                print("Nenhuma família cadastrada.")
            else:
                media_salario = soma_salario / total_familia
                media_numero_filhos = soma_filhos / total_familia

                print("Relatório:")
                print(f"Total de famílias: {total_familia}")
                print(f"Menor salário: {menor_salario}")
                print(f"Maior salário: {maior_salario}")
                print(f"Média de salário: {media_salario:.2f}")
                print(f"Média de número de filhos: {media_numero_filhos:.2f}")
            print("Saindo...")
            break