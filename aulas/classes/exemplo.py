from dataclasses import dataclass
import os
os.system("cls")

# Estrutura de dados: Classe
@dataclass
class Pessoa:
    nome: str
    idade: int
    cpf: str = "000.000.000-00" 

@dataclass
class pet:
    nome: str
    idade: int
    peso: float

pessoa1 = Pessoa(nome="João", idade=30, cpf="123.456.789-00")
pet1 = pet(nome="Rex", idade=5, peso=10.5)

print("Exibindo dados da pessoa:")
print(f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\nCPF: {pessoa1.cpf}")

print("\nExibindo dados do pet:")
print(f"Nome: {pet1.nome}\nIdade: {pet1.idade}\nPeso: {pet1.peso} kg")