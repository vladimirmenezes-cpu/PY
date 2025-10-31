import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Autor:
    nome: str 
    bio: str

@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor

    def exibir_dados(self):
        print(f"- Titulo do livro é: {self.titulo}")
        print(f"Ano de publicação é: {self.ano}")
        print(f"Livro produzido por {self.autor.nome}")

lista_dados = []
for i in range (2): 
    print(f"\n Cadastro do livro {i + 1}")

    pessoa = Livro(titulo=input("Qual o titulo do livro? "),
                   ano=int(input("Qual o ano de publicação do livros: ")),
                   autor=Autor(
                    nome=input("Qual nome do autor do livro: "),
                    bio=input("Escreva uma pequena biografia do autor: ")  
                    ))
    lista_dados.append(pessoa)
    os.system("cls")

os.system("cls")
for i, pessoa in enumerate(lista_dados, start=1):
    print(f"\n Livro {i}:")
    pessoa.exibir_dados()


