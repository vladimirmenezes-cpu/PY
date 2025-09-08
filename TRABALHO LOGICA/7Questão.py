import os
os.system("cls")

produto = input("Digite o Nome do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitario do produto: "))

valot_total = quantidade * preco_unitario

if quantidade <= 5:
    desconto = 2  
elif quantidade <= 10: 
    desconto = 3 
else:  
    desconto = 5 

valor_desconto = valot_total * (desconto / 100)

total_a_pagar = valot_total - valor_desconto

print("--- NOTA FISCAL ---")
print(f"Produto: {produto}")
print(f"Quantidade: {quantidade} unidades")
print(f"Preço Unitário: R$ {preco_unitario: }")
print(f"Valor total: R$ {valot_total: } ")
print(f"Desconto aplicado ({desconto}%): - R$ {valor_desconto}")
print(f"TOTAL A PAGAR: R$ {total_a_pagar: }")

