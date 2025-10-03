import os
os.system("cls")
# Função com passagem de parametros
def saudacao(nome, idade, altura, peso):
    print(f"Olá, {nome}! Bem-vindo(a) nosso site.")
    print(f"Sua idade é {idade} anos.: ")
    print(f"Sua altura é {altura}: ")
    print(f"Seu peso é: {peso}: " )

def limpeza():
    os.system("cls")



nome = input("Fala seu nome: ")

limpeza()
idade = int(input("Digite sua idade: "))

limpeza()
altura = float(input("Digite sua altura: "))

limpeza()
peso = float(input("Digite seu peso: "))

limpeza()
saudacao(nome, idade, altura, peso)