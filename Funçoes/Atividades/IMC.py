import os
os.system("cls")

def imc(peso, altura):
    os.system("cls")
    print(f"Calculando IMC para: {peso} kg e {altura} m")
    return peso / (altura ** 2)

def resultado_imc(imc):
    if imc < 18.5:
        print("consulte uma nutricionista para orientações")
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        print("mantenha habitos saudaveis!")
        return "Peso normal"
    elif 25 <= imc < 30:
        print("Considere uma dieta balanceada e atividade fisica")
        return "Sobrepeso"
    elif imc >= 30:
        print("Consulte um nutricionista para orientação")
        return "Obesidade"
    

peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))

imc_resultado = imc(peso, altura)
print(f"O IMC é: {imc_resultado:.2f}")
print(f"Classificação: {resultado_imc(imc_resultado)}")