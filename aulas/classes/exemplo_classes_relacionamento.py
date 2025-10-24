import os 
from dataclasses import dataclass

os.system("cls")

@dataclass
class Endereco:
    logradouro: str
    numero: int

@dataclass
class Cliente:
    nome: str
    endereco: Endereco

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Logradouro: {self.endereco.logradouro}")
        print(f"Número: {self.endereco.numero}")


cliente1 = Cliente(nome="Marta", 
                   endereco=Endereco(
                       logradouro="Rua A",
                   numero=23))

