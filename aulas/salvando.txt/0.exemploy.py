import os 
os.system("cls")

# Texto que desejo salvar
texto = input("Digite seu nome: ")

# Definir nome do arquivo para salvar.

nome_arquivo = "exemplo0.txt"

# Comadnos para salvar.

# a = APPEND
# w = ESCREVER
with  open(nome_arquivo, "A") as meu_arquivo:
    meu_arquivo.write(texto)
    print("Salvo com sucesso!")
