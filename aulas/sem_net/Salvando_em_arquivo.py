import os 
from dataclasses import dataclass
os.system("cls")


@dataclass
class Paciente:
    nome: str
    idade: int
    peso: int
    altura: float
    cpf: float

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade} \nPeso: {self.peso} \nAltura: {self.altura} \nCPF: {self.cpf}")

lista_de_pacientes = []
quantidade_de_pacientes = 1

for i in range(quantidade_de_pacientes):
    paciente =  Paciente(
        nome= input("Digite seu nome:"),
        idade= int(input("Digite sua idade:")),
        peso= int(input("Digite seu peso:")),
        altura=float(input("Digite sua altura:")),
        cpf= float(input("Digite seu cpf:"))
    )
    lista_de_pacientes.append(paciente)
    print()

nome_do_arquivo = "Dados_paciente.csv"
with open(nome_do_arquivo, "w") as arquivo_paciente:
    for paciente in lista_de_pacientes:
        arquivo_paciente.write(f"{paciente.nome},{paciente.idade},{paciente.peso}, {paciente.altura}, {paciente.cpf}\n ")
        print("Dados salvos com sucesso,")


#print("\n Exibindo lista de pacientes:")
#for paciente in lista_de_pacientes:
#    paciente.exibir_dados()

print("\nExibindo todos os pacientes: ")
try:
    # read - r - leitura
    with open(nome_do_arquivo, "r") as arquivo:
        lista_todos_paciente = arquivo.readlines()
        for paciente in lista_de_pacientes:
            print(f"- {paciente.strip()}")
except FileNotFoundError:
    print("O arquivo não foi encontrado.")

    