import os 
os.system("cls")

#Crie um programa que leia 4 notas,armazenando em um vetor e calcule media aritmetica
prato = []

print("""
Bem-vindo Ao Vitinho_Do_Grau, O melhor RESTAURANTE DE SALVAOR
      \t
          Escolha seu pedido e informe seu código!
      """)

print("""
 ================MENU================
      
      Codígo \t Prato \t           Valor
      \t
       1      Picanha           R$ 25.00
      
       2      Lasanha            R$ 20.00
      
       3      Strogonoff         R$ 18.00
      
       4      Bife Acebolado    R$ 89.00
      
       5     Pão com ovo         R$ 5.00
""")

menu = int(input("Digite o numero do pedido: "))
soma = 0
 
match menu:
    case 1:
        print("Picanha.........25.00")
        soma += 25.00
    case 2:
        print("Lasanha.........20.00")
        soma += 20.00
    case 3:
        print("Strogonoff.........18.00")
        soma += 18.00
    case 4:
        print("Bife acebolado.........15.00")
        soma += 15.00
    case 5:
        print("Pão com ovo.........5.00")
        soma += 5.00
    case _:
        print("Opção inválida")
while True:
    mais = input("Deseja pedir mais algo? (s/n): ").lower()
    if mais == 's':
        menu = int(input("Digite o numero do pedido: "))
        match menu:
            case 1:
                print("Picanha.........25.00")
                soma += 25.00
            case 2:
                print("Lasanha.........20.00")
                soma += 20.00
            case 3:
                print("Strogonoff.........18.00")
                soma += 18.00
            case 4:
                print("Bife acebolado.........15.00")
                soma += 15.00
            case 5:
                print("Pão com ovo.........5.00")
                soma += 5.00
            case _:
                print("Opção inválida")
        prato.append(menu)
    elif mais == 'n':
        break

else:
    print("Opção inválida, digite 's' ou 'n'.")        
       

print(f"Total a pagar: {soma:.2f}")