from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class DadosBasicos:
    nome: str
    email: str 
    telefone: int 
    endereco: str

print("\n Pedindo dados do úsuario")
pessoa1 = DadosBasicos(nome= input("Digite seu nome: "),
                       email=input("Digite seu email: "),
                       telefone=int(input("Digite seu numero de telefone: ")),
                       endereco=input("Digite seu endereço:"))

os.system("cls")
print("\nExibindo dados coletados")
print(f"Nome: {pessoa1.nome}\nEmail: {pessoa1.email}\nTelefone: {pessoa1.telefone}\nEndereço: {pessoa1.endereco}")