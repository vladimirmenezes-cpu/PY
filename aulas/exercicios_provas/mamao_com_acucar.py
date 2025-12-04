import os
import time
from dataclasses import dataclass
os.system("cls || clear")

lista_clientes = []
lista_produtos = []

@dataclass
class Cliente:
    nome: str 
    email: str
    telefone: int
    endereco: str 

    def exibir_dados(self):
        print(f"Nome do cliente: {self.nome}")
        print(f"Email do cliente: {self.email}")
        print(f"Telefone do cliente: {self.telefone}")
        print(f"Endereço do cliente: {self.endereco}")

def lista_branco(lista_clientes):
    if not lista_clientes:
        print("Não há Clientes cadastrados. ")
        return True 
    return False


def adicionar_cliente(lista_clientes):
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    telefone = int(input("Digite seu telefone: "))
    endereco = input("Digite seu endereço: ")
    novo_cliente = Cliente(nome=nome, email=email, telefone=telefone, endereco=endereco)
    lista_clientes.append(novo_cliente)
    print("Cadastro realizado com sucesso!!")

def encontrar_cliente(lista_clientes, telefone_busca):
    telefone_busca = telefone_busca
    for cliente in lista_clientes:
        if cliente.telefone == telefone_busca:
            return cliente
    return None

def mostrar_todos_clientes(lista_clientes):
    if lista_branco(lista_clientes):
        return

    print("\nLista de todos os clientes:")
    for cliente in lista_clientes:
        cliente.exibir_dados()
        print("---------")

def atualizar_cliente(lista_clientes):
    if lista_branco(lista_clientes):
        return
    
    mostrar_todos_clientes(lista_clientes)
    telefone_busca = int(input("Digite o telefone do cliente que deseja atualizar os dados: "))
    cliente_para_update = encontrar_cliente(lista_clientes, telefone_busca)

    if cliente_para_update is None:
        print("\nCliente não encontrado.")
        return

    print("\nDigite os novos dados (deixe em branco para manter o valor atual):")
    novo_nome = input(f"Novo nome (Atual: {cliente_para_update.nome}): ")
    novo_email = input(f"Novo email (Atual: {cliente_para_update.email}): ")
    novo_telefone = input(f"Novo telefone (Atual: {cliente_para_update.telefone}): ")
    novo_endereco = input(f"Novo endereço (Atual: {cliente_para_update.endereco}): ")

    if novo_nome.strip():
        cliente_para_update.nome = novo_nome
    if novo_email.strip():
        cliente_para_update.email = novo_email
    if novo_telefone.strip():
        cliente_para_update.telefone = int(novo_telefone)
    if novo_endereco.strip():
        cliente_para_update.endereco = novo_endereco

    print(f"\nDados do cliente '{telefone_busca}' atualizados com sucesso!")

def excluir_cliente(lista_clientes):
    if lista_branco(lista_clientes):
        return

    mostrar_todos_clientes(lista_clientes)

    telefone_busca = int(input("\nDigite o telefone do cliente que deseja excluir: "))

    cliente_excluir = encontrar_cliente(lista_clientes, telefone_busca) 

    if cliente_excluir:
        lista_clientes.remove(cliente_excluir)
        print(f"\nCliente com telefone '{telefone_busca}' excluído com sucesso!")
    else:
        print("\nCliente não encontrado.")

@dataclass
class Produto:
    nome: str
    quantidade: int
    lote: str
    validade: str

    def exibir_dados(self):
        print(f"Nome do produto: {self.nome}")
        print(f"Quantidade em estoque: {self.quantidade}")
        print(f"Lote do produto: {self.lote}")
        print(f"Validade do produto: {self.validade}")
    
def lista_branco_produtos(lista_produtos):
    if not lista_produtos:
        print("Não há Produtos cadastrados. ")
        return True 
    return False

def adicionar_produto(lista_produtos):
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade em estoque: "))
    lote = input("Digite o lote do produto: ")
    validade = input("Digite a validade do produto (DD-MM-AAAA): ")
    novo_produto = Produto(nome=nome, quantidade=quantidade, lote=lote, validade=validade)
    lista_produtos.append(novo_produto)
    print("Produto adicionado com sucesso!!")

def encontrar_produto(lista_produtos, lote_busca):
    lote_busca = lote_busca
    for produto in lista_produtos:
        if produto.lote == lote_busca:
            return produto
    return None

def mostrar_todos_produtos(lista_produtos):
    if lista_branco_produtos(lista_produtos):
        return

    print("\nLista de todos os produtos:")
    for produto in lista_produtos:
        produto.exibir_dados()
        print("---------")

def atualizar_produto(lista_produtos):
    if lista_branco_produtos(lista_produtos):
        return
    
    mostrar_todos_produtos(lista_produtos)
    lote_busca = input("Digite o lote do produto que deseja atualizar os dados: ")
    produto_para_update = encontrar_produto(lista_produtos, lote_busca)

    if produto_para_update is None:
        print("\nProduto não encontrado.")
        return

    print("\nDigite os novos dados (deixe em branco para manter o valor atual):")
    novo_nome = input(f"Novo nome (Atual: {produto_para_update.nome}): ")
    nova_quantidade = input(f"Nova quantidade (Atual: {produto_para_update.quantidade}): ")
    novo_lote = input(f"Novo lote (Atual: {produto_para_update.lote}): ")
    nova_validade = input(f"Nova validade (Atual: {produto_para_update.validade}): ")

    if novo_nome.strip():
        produto_para_update.nome = novo_nome
    if nova_quantidade.strip():
        produto_para_update.quantidade = int(nova_quantidade)
    if novo_lote.strip():
        produto_para_update.lote = novo_lote
    if nova_validade.strip():
        produto_para_update.validade = nova_validade

    print(f"\nDados do produto '{lote_busca}' atualizados com sucesso!")

def excluir_produto(lista_produtos):
    if lista_branco_produtos(lista_produtos):
        return

    mostrar_todos_produtos(lista_produtos)

    lote_busca = input("\nDigite o lote do produto que deseja excluir: ")

    produto_excluir = encontrar_produto(lista_produtos, lote_busca) 

    if produto_excluir:
        lista_produtos.remove(produto_excluir)
        print(f"\nProduto com lote '{lote_busca}' excluído com sucesso!")
    else:
        print("\nProduto não encontrado.")

def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Gerenciar Clientes")
        print("2. Gerenciar Produtos")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            menu_clientes()
        elif escolha == "2":
            menu_produtos()
        elif escolha == "3":
            print("Saindo do programa...")
            time.sleep(1)
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_clientes():
    while True:
        print("\n--- Menu Clientes ---")
        print("1. Adicionar Cliente")
        print("2. Mostrar Todos os Clientes")
        print("3. Atualizar Cliente")
        print("4. Excluir Cliente")
        print("5. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_cliente(lista_clientes)
        elif escolha == "2":
            mostrar_todos_clientes(lista_clientes)
        elif escolha == "3":
            atualizar_cliente(lista_clientes)
        elif escolha == "4":
            excluir_cliente(lista_clientes)
        elif escolha == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_produtos():
    while True:
        print("\n--- Menu Produtos ---")
        print("1. Adicionar Produto")
        print("2. Mostrar Todos os Produtos")
        print("3. Atualizar Produto")
        print("4. Excluir Produto")
        print("5. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_produto(lista_produtos)
        elif escolha == "2":
            mostrar_todos_produtos(lista_produtos)
        elif escolha == "3":
            atualizar_produto(lista_produtos)
        elif escolha == "4":
            excluir_produto(lista_produtos)
        elif escolha == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_principal()