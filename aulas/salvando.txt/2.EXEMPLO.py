import os 
from dataclasses import dataclass
os.system("cls")

@dataclass
class Livro:
    nome: str
    autor: str
    categoria : str
    preco: float

lista_livros = []

print("Solicitando dados do aluno. ")
for i in range(3):
    livro = Livro(
        nome= input("Digite o nome do livro: "),
        autor=input("Digite o nome do autor: "),
        categoria=input("Digite a categoria do livro: "),
        preco=float (input("Digite o preço do livro: "))
    )
    os.system("cls")
    lista_livros.append(livro)

print()
print("Salvando dados. ")
arquivo = "catalogo_livros.txt"

with open(arquivo, "a") as arquivo_catalogo:
    for livro in lista_livros:
        arquivo_catalogo.write(f"{livro.nome},{livro.autor},{livro.categoria},{livro.preco}  \n")
    print("Salvo com sucesso")