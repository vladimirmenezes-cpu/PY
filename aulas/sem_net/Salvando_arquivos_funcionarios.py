import os 
from dataclasses import dataclass
os.system("cls")


@dataclass
class Funcionario:
    nome: str
    nascimento: int
    rg: int
    cpf: float

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nNascimento: {self.nascimento} \nRG: {self.rg} \nCPF: {self.cpf}")

lista_de_funcionario = []
quantidade_de_funcionario = 1

for i in range(quantidade_de_funcionario):
    # A entrada de dados precisa de conversão de tipo ANTES da criação do objeto
    nome_input = input("Digite seu nome:")
    nascimento_input = input("Digite sua data de nascimento (apenas números, ex: 2000):")
    rg_input = input("Digite seu RG (apenas números):")
    cpf_input = input("Digite seu cpf:")
    
    funcionario = Funcionario(
        nome=nome_input,
        nascimento=int(nascimento_input),
        rg=int(rg_input),
        cpf=float(cpf_input)
    )
    lista_de_funcionario.append(funcionario)
    print()

nome_do_arquivo = "Funcionarios.csv"
# CORREÇÃO: Limpando a string de escrita para garantir exatamente 4 campos separados por vírgula
with open(nome_do_arquivo, "a", encoding="utf-8") as arquivo_funcionario:
    for funcionario in lista_de_funcionario:
        arquivo_funcionario.write(f"{funcionario.nome},{funcionario.nascimento},{funcionario.rg},{funcionario.cpf}\n")
        print("Dados salvos com sucesso.")


print("\nExibindo todos os funcionarios: ")
lista = []
try:
    with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo:
        lista_todos_funcionarios = arquivo.readlines()
        
        for linha in lista_todos_funcionarios:
            # CORREÇÃO: Verifica se a linha não está vazia antes de tentar desempacotar
            if linha.strip():
                # Desempacotamento de 4 campos estritos, usando .strip() para limpar
                nome, nascimento, rg, cpf = linha.strip().split(",")
                
                # Criação do objeto com os tipos convertidos
                dados_paciente = Funcionario(
                    nome=nome, 
                    nascimento=int(nascimento), 
                    rg=int(rg), 
                    cpf=float(cpf)
                )
                lista.append(dados_paciente)
    
    for paciente in lista:
        paciente.exibir_dados()
        
except FileNotFoundError:
    print("O arquivo não foi encontrado")
except ValueError:
    print("Erro ao converter dados. Verifique se o arquivo .csv contém exatamente 4 campos numéricos por linha.")