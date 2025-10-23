from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class DadosBasicos:
    nome: str
    idade: int
    peso: float
    altura: float

print("Solicitando dados da pessoa:")
pessoa1 = DadosBasicos(nome=input("Digite seu nome:"),
                 idade=int(input("Digite sua idade:")),
                 peso=float(input("Digite seu peso (kg):")),
                 altura=float(input("Digite sua altura (m):")))

os.system("cls")
print("\nExibindo dados basicos da pessoa:")
print(f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\nPeso: {pessoa1.peso}\nAltura: {pessoa1.altura}")
