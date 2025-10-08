import os
import time

# Função sem parâmetros e sem retorno.
def limpa_tela():
    time.sleep(3) # Espera 3 segundos.
    os.system("cls")

def multiplicacao(n1):
    return n1 * 100

def mostrar_resultado(multi):
    print(f"Resultado em centimentros: {multi} cm")

limpa_tela()
primeiro_numero = float(input("Digite o numero para converter em Centimetros: "))

multi = multiplicacao(primeiro_numero)
mostrar_resultado(multi)