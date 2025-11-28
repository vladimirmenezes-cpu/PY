import os
import time
from dataclasses import dataclass
os.system("cls || clear")

listaclientes = []

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

    def mostrar_dados(self):
        print(f"Nome do cliente: {self.nome}")
        print(f"E-mail do cliente: {self.email}")
        print(f"Telefone do cliente: {self.telefone}")

def lista_esta_vazia(lista_clientes):
    if not lista_clientes:
        print("Não há clientes cadastrados.")
        return True
    return False

def adicionar_cliente(lista_clientes):
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o e-mail do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    novo_cliente = Cliente(nome=nome, email=email, telefone=telefone)
    lista_clientes.append(novo_cliente)
    print("Cliente adicionado com sucesso!")

def encontra_cliente_pornome(lista_clientes, nome_busca):
    nome_busca_lower = nome_busca.lower()
    for cliente in lista_clientes:
        if cliente.nome.lower() == nome_busca_lower:
            return cliente
    return None

def mostrar_todos_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    
    print("\nLista de todos os clientes:")
    for cliente in lista_clientes:
        cliente.mostrar_dados()
        print("----------------")

def atualizar_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    
    mostrar_todos_clientes(lista_clientes)
    nome_busca = input("Digite o nome do cliente que deseja atualizar: ")
    cliente_para_update = encontra_cliente_pornome(lista_clientes, nome_busca)

    if cliente_para_update is None:
        print("\nCliente não encontrado.")
        return

    print("\nDigite os novos dados do cliente (deixe em branco para manter):")

    novo_nome = input(f"Novo nome (Atual: {cliente_para_update.nome}): ")
    novo_email = input(f"Novo e-mail (Atual: {cliente_para_update.email}): ")
    novo_telefone = input(f"Novo telefone (Atual: {cliente_para_update.telefone}): ")

    if novo_nome.strip():
        cliente_para_update.nome = novo_nome
    if novo_email.strip():
        cliente_para_update.email = novo_email
    if novo_telefone.strip():
        cliente_para_update.telefone = novo_telefone

    print(f"\nDados do cliente '{nome_busca}' atualizados com sucesso!")

def excluir_cliente(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    
    mostrar_todos_clientes(lista_clientes)
    
    nome_busca = input("\nDigite o nome do cliente que deseja excluir: ")

    cliente_para_excluir = encontra_cliente_pornome(lista_clientes, nome_busca)

    if cliente_para_excluir:
        lista_clientes.remove(cliente_para_excluir)
        print(f"\nCliente {cliente_para_excluir.nome} excluído com sucesso!")
    else:
        print("\nCliente não encontrado.")

while True:
    print("""
Gerenciamento de clientes
1. Adicionar cliente
2. Mostrar todos os clientes
3. Atualizar cliente
4. Excluir cliente
0. Sair
""")

    try:
        opcao = int(input("Digite uma das opções acima: "))
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
        continue

    match opcao:
        case 1:
            adicionar_cliente(listaclientes)
        case 2:
            mostrar_todos_clientes(listaclientes)
        case 3:
            atualizar_clientes(listaclientes)
        case 4:
            excluir_cliente(listaclientes)
        case 0:
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida. Tente novamente.")

    time.sleep(4)
    os.system("cls || clear")

          
