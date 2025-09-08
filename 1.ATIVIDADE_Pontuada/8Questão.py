import os
os.system("cls")

print("Cores disponíveis: Verde, Azul, Amarelo, Vermelho")

cor = input("Digite a cor do CD para ver o preço: ")

match cor:
    case "Verde":
        print("O CD da cor Verde custa R$ 10.00")
    case "Azul":
        print("O CD da cor azul custa R$ 20.00")
    case "Amarelo":
        print("O CD da cor amarelo custa R$ 30.00")
    case "Vermelho":
        print("O CD da cor vermelha custa R$ 40.00")
    case _:
        print("Opção invalida")