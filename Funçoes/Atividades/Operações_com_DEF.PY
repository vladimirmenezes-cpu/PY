import os
import time

# Função sem parâmetros e sem retorno.
def limpa_tela():
    time.sleep(3) # Espera 3 segundos.
    os.system("cls")

# Função com parâmetros e com retorno.
def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def divisao(n1, n2):
    return n1 / n2 if n2 != 0 else "Divisão por zero."

def multiplicacao(n1, n2):
    return n1 * n2

# Função com parâmetros e sem retorno.
def mostrar_resultado(soma, subtrair, divisao, multiplicacao):
    print(f"Resultado: {soma}")
    print(f"Resultado Subtração: {subtrair}")
    print(f"Resultado Divisão: {divisao}")
    print(f"Resultado Multiplicação: {multiplicacao}")

limpa_tela()
primeiro_numero = int(input("Digite o primiero numero: "))
segundo_numero = int(input("Digite o Segundo numero: "))

soma = somar(primeiro_numero, segundo_numero)
menos = subtrair(primeiro_numero, segundo_numero)
dividir = divisao(primeiro_numero, segundo_numero)
multi = multiplicacao(primeiro_numero, segundo_numero)


mostrar_resultado(soma, menos, dividir, multi)