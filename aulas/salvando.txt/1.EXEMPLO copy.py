import os 
from dataclasses import dataclass
os.system("cls")

@dataclass
class Aluno:
    nome: str
    idade: int
    email: str
    telefone: int

quantiade_alunos = 2
lista_alunos = []

print("Solicitando dados do aluno. ")
for i in range(quantiade_alunos):
    aluno = Aluno(
        nome= input("Digite seu nome: "),
        idade=int(input("Digite sua idade: ")),
        email=input("Digite seu email: "),
        telefone=int(input("Digite seu telefone: "))
    )
    os.system("cls")
    lista_alunos.append(aluno)

print()
print("Salvando dados. ")
arquivo = "dados_alunos.txt"

with open(arquivo, "a") as arquivo_alunos:
    for aluno in lista_alunos:
        arquivo_alunos.write(f"{aluno.nome},{aluno.idade},{aluno.email},{aluno.telefone}  \n")
    print("Salvo com sucesso")