import os
os.system("cls")

lista_notas = []

def calcular_media(lista_notas):
    resultado = sum(lista_notas) / 2
    return resultado

def resultado_final(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

for i in range(2):
    nota = float(input(f"digite a {i+1}ª nota: "))
    os.system("cls")
    if nota < 0 or nota > 10:
        os.system("cls")
        print("nota inválida, digite uma nota entre 0 e 10")
        nota = float(input(f"digite a {i+1}ª nota: "))
    lista_notas.append(nota)

media = calcular_media(lista_notas)
os.system("cls")
print(f"A média das notas é: {media:.2f}")
print(f"Resultado final: {resultado_final(media)}")