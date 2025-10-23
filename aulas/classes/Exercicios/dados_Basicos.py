from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class DadosBasicos:
    nome: str
    idade: int
    peso: float
    altura: float

pessoa1 = DadosBasicos(
    nome=input(f"Digite o nome da pessoa: "),
    idade=int(input(f"Digite a idade da pessoa: ")),
    peso=float(input(f"Digite o peso da pessoa (kg): ")),
    altura=float(input(f"Digite a altura da pessoa (m): "))
)

os.system("cls")
print("Exibindo dados basicos da pessoa:")
print(f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\nPeso: {pessoa1.peso}\nAltura: {pessoa1.altura}")
