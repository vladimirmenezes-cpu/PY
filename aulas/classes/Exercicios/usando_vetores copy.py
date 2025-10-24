import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class dados:
    nome: str
    cpf: str
    telefone: str

    def mostrar_dados(self):
        print("\n== Exibindo dados == ")
        print(f" Nome: {self.nome}\n CPF: {self.cpf}\n Telefone: {self.telefone}")

    def dados_marketing(self):
        print("\n== Dados para o marketing ==")
        print(f"\nTelefone: {self.telefone}")

print("Pedindo dados para os úsuarios")
lista_dados = []

for i in range(3):
    cliente = dados(nome= input(f"\n{i + 1} - Digite seu nome: "),
                    cpf=input(f"\n{i + 1} - Digite seu cpf: "),
                    telefone=input(f"\n{i + 1} - Digite seu telefone: "))
    os.system("cls")
    lista_dados.append(cliente)

print("== MOSTRANDO DADOS ==")

for cliente in lista_dados:
    cliente.mostrar_dados()

for cliente in lista_dados:
    cliente.dados_marketing()

    
