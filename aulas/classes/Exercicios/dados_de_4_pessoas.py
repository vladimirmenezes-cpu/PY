import os
from dataclasses import dataclass
os.system("cls")
 
@dataclass
class Dados_identidade:
    nome: str
    idade: int
    peso: float
    altura: float

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso}")
        print(f"Altura: {self.altura}")

lista_dados = []

contador = int(input(" insira a quantidade de pessoas que vc quer cadastrar"))

for i in range(contador):
    pessoa = Dados_identidade(nome= input(f"\nDigite seu nome: "),
                              idade=int(input("Digite sua idade: ")),
                              peso=float(input("Digite seu peso: ")),
                              altura=float(input("Digite sua altura: "))
                              )
    lista_dados.append(pessoa)

print("== Mostrando dados ==")

for pessoa in lista_dados:
    pessoa.mostrar_dados()


