import os
os.system("cls")

# Faça um algoritmo que mostre um menu com opções de um cardápio de restaurante.
# Após a escolha do prato, o sistema deve perguntar se o usuário deseja pedir
# mais alguma coisa. Se a resposta for sim, o menu deve ser mostrado novamente.
# Caso contrário, o sistema deve mostrar o valor total do pedido.



print("""
Bem-vindo Ao Vitinho_Do_Grau, O melhor RESTAURANTE DE SALVAOR
      \t
          Escolha seu pedido e informe seu código!
      """)

print("""
 ================MENU================
      
      Codígo \t Prato \t           Valor
      \t
       1      Pizza de Zucchini  R$ 89.00
      
       2      Pizza de 4 queijos  R$ 79.00
      
       3      Pizza de Atum      R$ 75.00
      
       4  Pizza de Pepperoni c/Mel  R$ 89.00
      
       5    Pizza de Camarão VG   R$ 99.99
""")

menu = int(input("Digite o codigo do seu pedido:"))
soma = 0 

match menu:
    case 1:
        print("Voce escolheu Pizza de Zucchini por R$ 89.00")
        soma += 89.00
    case 2:
        print("Voce escolheu Pizza de 4 queijos por 79.00") 
        soma += 79.00
    case 3:
        print("Voce escolheu Pizza de Atum por R$ 75.00")
        soma += 75.00
    case 4:
        print("Voce escolheu a Pizza de Pepperoni c/Mel R$ 89.00")
        soma += 89.00
    case 5:
        print("Voce escolheu Pizza de Camarão VG por R$ 99.99")
        soma += 99.99
        

while True:
    novo = input("Deseja realizar outro pedido?(S/N)")
    if novo == 'S':
        menu = int(input("Digite o codigo do seu pedido:"))
        match menu:
            case 1:
                print("Voce escolheu Pizza de Zucchini por R$ 89.00")
                soma += 89.00
            case 2:
                print("Voce escolheu Pizza de 4 queijos por 79.00")
                soma += 79.00
            case 3:
                print("Voce escolheu Pizza de Atum por R$ 75.00")
                soma += 75.00
            case 4:
                print("Voce escolheu a Pizza de Pepperoni c/Mel R$ 89.00")
                soma += 89.00
            case 5:
                print("Voce escolheu Pizza de Camarão VG por R$ 99.99")
                soma += 99.99
    elif novo == 'N':
        print("Obrigado por escolher o Vitinho_Do_Grau, volte sempre!")
        break

print(f"O valor total do seu pedido é R$ {soma:.2f}")