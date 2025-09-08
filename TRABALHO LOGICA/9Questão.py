import os
os.system("cls")

renda = float(input("Digite sua renda mensal: R$ "))
valor_emprestimo = float(input("Digite o valor do empréstimo desejado: R$ "))
prestacoes = int(input("Em quantas prestações você quer pagar? "))

limite_emprestimo = renda * 10
limite_prestacao = renda * 0.30

valor_prestacao = valor_emprestimo / prestacoes

if (valor_emprestimo <= limite_emprestimo) and (valor_prestacao <= limite_prestacao):

     print("\nParabéns! Seu empréstimo foi CONCEDIDO.")
     print(f"O valor de cada uma das {prestacoes} prestações será de R$ {valor_prestacao:.2f}")
else:
     print("Desculpe, seu empréstimo não foi concedido no momento.")