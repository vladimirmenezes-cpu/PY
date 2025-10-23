from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class pessoa:
    nome: str
    email: str 
    endereco: str

    def mostrar_dados(self):
        print("\nExibindo dados coletados")
        print(f"Nome: {self.nome}\nEmail: {self.email}\nEndereço: {self.endereco}")

    def mostrar_nome(self):
        print("Exibindo dados de marketink.")
        print(f"Nome: {self.nome}")

print("\n Pedindo dados do úsuario")
lista_pessoa = []

for i in range(2):
    pessoa = pessoa(nome= input("Digite seu nome: "),
                       email=input("Digite seu email: "),
                       endereco=input("Digite seu endereço:"))
    lista_pessoa.append(pessoa)



print("\n= Exibindo dados = ")
for pessoa in lista_pessoa:
    pessoa.mostrar_dados()

print("\n= Exibindo dados = ")
for pessoa in lista_pessoa:
    pessoa.mostrar_dados()