from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class DadosBasicos:
    nome: str
    email: str 
    telefone: int 
    endereco: str

    def mostrar_dados(self):
        os.system("cls")
        print("\nExibindo dados coletados")
        print(f"Nome: {self.nome}\nEmail: {self.email}\nTelefone: {self.telefone}\nEndereço: {self.endereco}")

print("\n Pedindo dados do úsuario")
pessoa1 = DadosBasicos(nome= input("Digite seu nome: "),
                       email=input("Digite seu email: "),
                       telefone=int(input("Digite seu numero de telefone: ")),
                       endereco=input("Digite seu endereço:"))

print("\n Pedindo dados do úsuario 2")
pessoa2 = DadosBasicos(nome= input("Digite seu nome: "),
                       email=input("Digite seu email: "),
                       telefone=int(input("Digite seu numero de telefone: ")),
                       endereco=input("Digite seu endereço:"))

def mostrar_resultado(pessoa1, pessoa2):
    print(f"Exibindo dados coletados:\n Nome: {pessoa1.nome}\nEmail: {pessoa1.email}\nTelefone: {pessoa1.telefone}\nEndereço {pessoa1.endereco}")
    print(f"Exibindo dados coletados dois:\n Nome: {pessoa2.nome}\nEmail: {pessoa2.email}\nTelefone: {pessoa2.telefone}\nEndereço {pessoa2.endereco}")

mostrar_resultado(pessoa1, pessoa2)