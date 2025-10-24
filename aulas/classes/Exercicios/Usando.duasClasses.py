import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str 


@dataclass
class Dados_identidade:
    nome: str
    email: str 
    endereco: Endereco

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Logradouro: {self.endereco.logradouro}")
        print(f"Número da casa: {self.endereco.numero}")
        print(f"Cidade: {self.endereco.cidade}")

pessoa1 = Dados_identidade(nome= input("Digite seu nome:"),
                           email=input("Digite seu melhor email:"),
                           endereco=Endereco(
                            logradouro=input("Digite seu logradouro:"),
                            numero=int(input("Digite o numero da casa: ")),
                            cidade=input("Digite sua cidade:")
                           
                           ))

print("== Exibindo dados ==")
pessoa1.mostrar_dados()
