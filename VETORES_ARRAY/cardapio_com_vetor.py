import os 
os.system("cls")

import os
os.system("cls")

# Vetores (listas) com dados do cardápio
codigos = [1, 2, 3, 4, 5, 6, 7, 8]
pratos = [
    "Picanha", "Lasanha", "Strogonoff", "Bife acebolado",
    "Pão com ovo", "Pudim", "Casquinha", "Bolo de pote"
]
valores = [25.00, 20.00, 18.00, 15.00, 5.00, 12.00, 6.00, 10.00]

# Listas para armazenar os pedidos feitos
pedidos = []
valores_pedidos = []

soma = 0.0
continuar = 's'

while continuar == 's':
    print("\n======== Cardápio ========")
    for i in range(len(pratos)):
        print(f"{codigos[i]} - {pratos[i]:20} R$ {valores[i]:.2f}")

    menu = input("\nDigite o número do pedido: ")

    if menu.isdigit():
        menu = int(menu)
        if menu in codigos:
            i = codigos.index(menu)
            print(f"{pratos[i]} selecionado - R$ {valores[i]:.2f}")
            pedidos.append(pratos[i])
            valores_pedidos.append(valores[i])
            soma += valores[i]
        else:
            print("Código inválido.")
    else:
        print("Entrada inválida. Digite um número.")

    continuar = input("Deseja pedir mais algo? (s/n): ").lower()

# Mostrar resumo final do pedido
print("\n======= Pedido Final =======")
for i in range(len(pedidos)):
    print(f"{pedidos[i]:20} R$ {valores_pedidos[i]:.2f}")

print(f"\nTotal a pagar: R$ {soma:.2f}")
