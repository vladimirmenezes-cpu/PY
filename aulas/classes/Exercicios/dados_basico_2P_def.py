from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class pessoa:
    nome: str
    email: str 
    telefone: int 
    endereco: str

    def mostrar_dados(self):
        print("\nExibindo dados coletados")
        print(f"Nome: {self.nome}\nEmail: {self.email}\nTelefone: {self.telefone}\nEndereço: {self.endereco}")

print("\n Pedindo dados do úsuario")
pessoa1 = pessoa(nome= input("Digite seu nome: "),
                       email=input("Digite seu email: "),
                       telefone=int(input("Digite seu numero de telefone: ")),
                       endereco=input("Digite seu endereço:"))

print("\n Pedindo dados do úsuario 2")
pessoa2 = pessoa(nome= input("Digite seu nome: "),
                       email=input("Digite seu email: "),
                       telefone=int(input("Digite seu numero de telefone: ")),
                       endereco=input("Digite seu endereço:"))

print("\n = Exibindo dados =")
pessoa1.mostrar_dados()
pessoa2.mostrar_dados()