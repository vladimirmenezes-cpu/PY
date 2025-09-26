import os
os.system("cls")

pessoas = []
total_salario = 0
menor_idade = 0
maior_idade = 0
quantidade_mulheres_acima_5000 = 0

while True:
    print(""" Menu:
    1. Adicionar pessoa
    2. Exibir relatório
    3. Sair
    """)
    escolha = input("Escolha uma opção: ")

    match escolha:
        case "1":
            idade = int(input("Idade: "))
            sexo = input("Sexo (M/F): ").upper()
            salario = float(input("Salário: "))

            pessoas.append({"idade": idade, "sexo": sexo, "salario": salario})
            total_salario += salario

            if idade < menor_idade:
                menor_idade = idade
            if idade > maior_idade:
                maior_idade = idade
            
            if sexo == "F" and salario > 5000:
                quantidade_mulheres_acima_5000 += 1
            
        case "2":
            if len(pessoas) == 0:
                print("Nenhuma pessoa cadastrada.")
            else:
                media_salario = total_salario / len(pessoas)
                print(f"Média de salário: {media_salario:.2f}")
                print(f"Menor idade: {menor_idade}")
                print(f"Maior idade: {maior_idade}")
                print(f"Quantidade de mulheres com salário acima de 5000: {quantidade_mulheres_acima_5000}")
        
        case "3":
            print("Saindo...")
            break