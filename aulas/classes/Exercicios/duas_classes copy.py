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
pessoa1 = pessoa(nome= input("Digite seu nome: "),
                       email=input("Digite seu email: "),
                       endereco=input("Digite seu endereço:"))

print("\n Pedindo dados do úsuario")
pessoa2 = pessoa(nome= input("Digite seu nome: "),
                       email=input("Digite seu email: "),
                       endereco=input("Digite seu endereço:"))

pessoa1.mostra_dados()
pessoa1.mostrar_nome()
pessoa2.mostra_dados()
pessoa2.mostrar_nome()
 