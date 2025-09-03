import os
os.system("cls")

data = int(input("Digite um numero e descubra o mes:"))

match data:
    case 1:
        print("mes de Janeiro")
    case 2:
        print("Mes de Fevereiro")
    case 3:
        print("Mes de Março")
    case 4:
        print("Mes de Abril")
    case 5:
        print("Mes de Maio")
    case 6:
        print("Mes de Junho ")
    case 7:
        print("mes de Julho")
    case 8:
        print("Mes de Agosto")
    case 9:
        print("Mes de Setembro")
    case 10: 
        print("Mes de Outubro")
    case 11: 
        print("Mes de Novembro")
    case 12: 
        print("Mes de Dezembro")
    case _:
        print("Invalido")
