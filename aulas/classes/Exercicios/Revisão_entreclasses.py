import os 
from dataclasses import dataclass 
os.system("cls")

@dataclass
class   Endereco:
    logradouro: str
    numero: int

@dataclass
class Pessoa:
    nome: str
    idade: int
    endereco: Endereco

    def mostrar_dados(self):
        print(f"Seu nome é: {self.nome}")
        print(f"Sua idade é: {self.idade}")
        print(f"Sua logradouro é: {self.endereco.logradouro}")
        print(f"Numero da sua casa é: {self.endereco.numero}")

pessoa1 = Pessoa(nome=input("Qual seu nome?"),
                 idade=int(input("Qual sua idade?")),
                 endereco=Endereco(
                     logradouro=input("Digite seu logradouro: "),
                     numero=int(input("Digite o numero da sua casa: "))
                     
                 ))

print("--- MOSTRAR DADOS ---")
pessoa1.mostrar_dados()