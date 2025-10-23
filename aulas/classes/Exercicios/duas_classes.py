from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class pessoa:
    nome: str
    email: str 
    endereco: str

    def dados_entrega(self):
        print("\nExibindo dados coletados")
        print(f"Nome: {self.nome}\nEndereço: {self.endereco}")

    def dados_marketing(self):
        print("Exibindo dados de marketink.")
        print(f"Nome: {self.nome}\nEmail: {self.email}")

print("\n Pedindo dados do úsuario")
pessoa1 = pessoa(nome= input("Digite seu nome: "),
                       email=input("Digite seu email: "),
                       endereco=input("Digite seu endereço:"))

pessoa1.dados_entrega()
pessoa1.dados_marketing()
 

