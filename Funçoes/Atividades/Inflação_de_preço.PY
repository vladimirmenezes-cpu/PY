import os
import time

# Função sem parâmetros e sem retorno.
def limpa_tela():
    time.sleep(3) # Espera 3 segundos.
    os.system("cls")

def valor_inicial(n1):
    if n1 >= 100:
        return n1 * 0.2
    else:
        return n1 * 0.1

def mostrar_resultado(multi):
    print(f"Resultado final do produto: {multi}")

limpa_tela()
preco = int(input("Digite o preço do produto "))

limpa_tela()
multi = valor_inicial(preco) + preco
mostrar_resultado(multi)