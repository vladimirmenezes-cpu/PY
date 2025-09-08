import os
os.system("cls")

PRECO_GASOLINA = 6.59
PRECO_ALCOOL = 3.79

print("--- POSTO DE COMBUSTÍVEIS PYTHON ---")
print("Opções: A-álcool | G-gasolina")

tipo_combustivel = input("Digite o tipo de combustível (A ou G): ")
litros_vendidos = float(input("Digite a quantidade de litros vendidos: "))

match tipo_combustivel:
    case 'A':
        print("Combustível selecionado: Álcool")
        preco_s_desconto = litros_vendidos * PRECO_ALCOOL

        if litros_vendidos <= 25:
            desconto = 0.10
        else:
            desconto = 0.20
        
        valor_total = preco_s_desconto * (1 - desconto)

    case 'G':
        print("Combustivel selecioando: Gasolina")
        preco_s_desconto = litros_vendidos * PRECO_ALCOOL

        if litros_vendidos <= 25:
            desconto = 0.15
        else:
            desconto = 0.30

        valor_total = preco_s_desconto * (1 - desconto)
    
    case _:
        print("Opção invalida")

    
print (f"Total de litros: {litros_vendidos} L")
print(f"Valor a pagar: R$ {valor_total}")