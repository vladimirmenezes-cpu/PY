import os
os.system("cls")

valor_produto = float(input("Digite o valor do produto: R$ "))

print("\nEscolha a forma de pagamento:")
print("1 - Pagamento à vista")
print("2 - Pagamento a prazo")

opcao = int(input("Digite a opção desejada: "))

match opcao:
    case 1:
        valor_desconto = valor_produto * 0.10
        total_a_pagar = valor_produto - valor_desconto
        
        print("Pagamento à vista selecionado.")
        print(f"Valor do produto: R$ {valor_produto:}")
        print("Forma de pagamento: à vista")
        print(f"Valor do desconto: R$ {valor_desconto:}")
        print(f"Total a pagar: R$ {total_a_pagar:}")

    case 2:
        parcelas = int(input("Digite a quantidade de parcelas (até 6x): "))
        
        if 1 <= parcelas <= 6:
            valor_parcela = valor_produto / parcelas
            
            print("\nPagamento a prazo selecionado.")
            print(f"Valor do produto: R$ {valor_produto:}")
            print("Forma de pagamento: a prazo")
            print(f"Quantidade de parcelas: {parcelas}")
            print(f"Valor por parcela: R$ {valor_parcela:}")
            print(f"Total a prazo: R$ {valor_produto:}")
        else:
            print("Número de parcelas inválido. O máximo permitido é 6 vezes.")

    case _:
        print("Opção de pagamento inválida. Por favor, escolha 1 ou 2.")