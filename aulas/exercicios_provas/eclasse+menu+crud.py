import os
import time
from dataclasses import dataclass
os.system("cls || clear")

listafuncionarios = []

@dataclass
class Funcionarios:
    nome: str 
    nascimento: int
    cpf: int 
    funcao: str

    def exibir_dados(self):
        print(f"Nome do funcionario: {self.nome}")
        print(f"Data de nascimento do funcionario: {self.nascimento}")
        print(f"CPF do funcionario: {self.cpf}")
        print(f"Função do funcionario: {self.funcao}")

def lista_branco(listafuncionarios):
    if not listafuncionarios:
        print("Não há funcionarios cadastrados. ")
        return True 
    return False

def adicionar(listafuncionarios):
    nome = input("Digite seu nome: ")
    nascimento = input("Digite sua data de nascimento: ")
    cpf = input("Digite seu CPF: ")
    funcao = input("Digite seu cargo na empresa: ")
    novo_funcionario = Funcionarios(nome=nome, nascimento=nascimento, cpf=cpf, funcao=funcao)
    listafuncionarios.append(novo_funcionario)
    print("Cadastro realizado com sucesso!!")

def encontrar_funcionario(listafuncionarios, cpf_busca):
    cpf_busca = cpf_busca
    for funcionario in listafuncionarios:
        if funcionario.cpf == cpf_busca:
            return funcionario
    return None

def mostrar_todos_funcionarios(listafuncionarios):
    if lista_branco(listafuncionarios):
        return

    print("\nLista de todos os funcionarios:")
    for funcionario in listafuncionarios:
        funcionario.exibir_dados()
        print("---------")

def atualizar_funcionario(listafuncionarios):
    if lista_branco(listafuncionarios):
        return
    
    mostrar_todos_funcionarios(listafuncionarios)
    cpf_busca = input("Digite o CPF do funcionario  que deseja atualizar os dados: ")
    funcionario_para_update = encontrar_funcionario(listafuncionarios, cpf_busca)

    if funcionario_para_update is None:
        print("\nCliente não encontrado.")
        return

    print("\nDigite os novos dados do cliente (deixe em branco para manter):")

    novo_nome = input(f"Novo nome (Atual: {funcionario_para_update.nome}): ")
    novo_nascimento = input(f"Nova data de nascimento (Atual: {funcionario_para_update.nascimento}): ")
    novo_cpf = input(f"Novo CPF (Atual: {funcionario_para_update.cpf}): ")
    novo_funcao = input(f"Nova Função do funcionario (Atual: {funcionario_para_update.funcao}): ")

    if novo_nome.strip():
        funcionario_para_update.nome = novo_nome
    if novo_nascimento.strip():
        funcionario_para_update.email = novo_nascimento
    if novo_cpf.strip():
        funcionario_para_update.telefone = novo_cpf

    print(f"\nDados do cliente '{cpf_busca}' atualizados com sucesso!")


def excluir_funcionario(listafuncionarios):
    if lista_branco(listafuncionarios):
        return

    mostrar_todos_funcionarios(listafuncionarios)

    cpf_busca = input("\nDigite o cpf do funcionario que deseja excluir: ")

    funcionario_excluir = encontrar_funcionario(listafuncionarios, cpf_busca) 

    if funcionario_excluir:
        listafuncionarios.remove(funcionario_excluir)
        print(f"\nFuncionario {funcionario_excluir.cpf} excluido com sucesso!")
    else:
        print("\nFuncionario não encontrado.")


while True:
    print("""
    Gerenciamento de funcionario 
    1. Adicionar funcionarios
    2. Mostrar todos funcionarios cadastrado 
    3. Atualizar dados 
    4. Excluir dados do funcionario
    0. Sair
    """)

    try:
        opcao = int(input("Digite uma das opçõpes acima:"))
    except ValueError:
        print("Entrada invalida: Digite apenas numeros.")
        continue 

    match opcao:
        case 1:
            adicionar(listafuncionarios)
        case 2:
            mostrar_todos_funcionarios(listafuncionarios)
        case 3:
            atualizar_funcionario(listafuncionarios)
        case 4:
            excluir_funcionario(listafuncionarios)
        case 0:
            print("Saindo do programa....")
            break
        case _:
            print("opcao intalida. Tente novamente.")

    time.sleep(4)
    os.system("cls || clear")
