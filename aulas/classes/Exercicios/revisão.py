import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Cliente:
    nome: str
    endereco: str
    telefone: str


    def mostrar_dados_cliente(self):
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")

lista_de_cliente = []

for i in range(3):
    dados_cliente = Cliente(nome=input("Digite seu nome:"),
                   endereco=input("Digite seu endereço:"),
                   telefone=input("Digite seu telefone"))
    lista_de_cliente.append(dados_cliente)
    os.system("cls")    
        
for cliente in lista_de_cliente:
    cliente.mostrar_dados_cliente()

