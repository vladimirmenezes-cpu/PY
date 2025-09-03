import os
os.system("cls")

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

      ==========SOBREMESA==========
      
        Codígo \t Prato \t           Valor
      \t
       6    Pizza de Brigadeiro  R$ 68.00
      
       7    Pizza de Doce de leite R$ 79.00
      
       8   Pizza de Creme de pistache R$ 75.00
      
       9       Pizza de Paçoca   R$ 89.00
      
       0  Brownie c/ Sorbet de creme R$ 120.00
""")


codigo = int(input("Digite o codigo do seu pedido:"))


match codigo:
    case 1:
        print("Voce escolheu Pizza de Zucchini por R$ 89.00")
    case 2:
        print("Voce escolheu Pizza de 4 queijos por 79.00")
    case 3:
        print("Voce escolheu Pizza de Atum por R$ 75.00")
    case 4:
        print("Voce escolheu a Pizza de Pepperoni c/Mel R$ 89.00")
    case 5:
        print("Voce escolheu Pizza de Camarão VG por R$ 99.99")
    case 6:
        print("Voce escolheu Pizza de Brigadeiro por R$ 68.00 ")
    case 7:
        print("Voce escolheu pizza de doce de leite por R$ 79.00")
    case 8:
        print("Voce escolheu pizza de Creme de Pistache por R$ 75.00")
    case 9:
        print("Voce escolheu a Pizza de Paçoca por R$ 89.00")
    case 0: 
        print("Voce escolheu o Brownie c/ Sorbet de creme por R$ 120.00")