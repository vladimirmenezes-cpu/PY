import os
import time
from dataclasses import dataclass
os.system("cls || clear")

lista_estudante = []

@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str
    estado: str


@dataclass
class Dados_aluno:
    nome: str 
    nascimento: int
    ra: int 
    curso: str
    endereco: Endereco

    def exibir_dados(self):
        print(f"Nome do estudante: {self.nome}")
        print(f"Data de nascimento do estudante: {self.nascimento}")
        print(f"R.A do estudante: {self.ra}")
        print(f"Curso do estudante: {self.curso}")
        print(f"Logradouro do estudante: {self.endereco.logradouro}")
        print(f"Numero da casa do estudante: {self.endereco.numero}")
        print(f"Cidade do estudante: {self.endereco.cidade}")
        print(f"Estado do estudante: {self.endereco.estado}")

def lista_branco(lista_estudante):
    if not lista_estudante:
        print("Não há estudante cadastrados. ")
        return True 
    return False

def adicionar(lista_estudante):
    nome = input("Digite seu nome: ")
    nascimento = input("Digite sua data de nascimento: ")
    ra = int(input("Digite seu R.A de estudante: "))
    curso = input("Digite o curso que pertence: ")
    endereco=Endereco(
        logradouro=input("Digite seu logradouro:"),
        numero=int(input("Digite o numero da sua casa:")),
        cidade=input("Digite sua cidade de residencia: "),
        estado=input("Digite seu estado:")
    )
    novo_estudante = Dados_aluno(nome=nome, nascimento=nascimento, ra=ra, curso=curso,  endereco=endereco)
    lista_estudante.append(novo_estudante)
    print("Cadastro realizado com sucesso!!")

def encontrar_aluno(lista_estudante, ra_busca):
    ra_busca = ra_busca
    for estudante in lista_estudante:
        if estudante.ra == ra_busca:
            return estudante
    return None

def mostrar_todos_aluno(lista_estudante):
    if lista_branco(lista_estudante):
        return

    print("\nLista de todos os estudantes")
    for estudante in lista_estudante:
        estudante.exibir_dados()
        print("---------")

def atualizar_estudante(lista_estudante):
    if lista_branco(lista_estudante):
        return
    
    mostrar_todos_aluno(lista_estudante)
    ra_busca = int(input("Digite o R.A do estudante  que deseja atualizar os dados: "))
    estudante_para_update = encontrar_aluno(lista_estudante, ra_busca)

    if estudante_para_update is None:
        print("\nEstudante não encontrado.")
        return

    print("\nDigite os novos dados do aluno (deixe em branco para manter):")

    novo_nome = input(f"Novo nome (Atual: {estudante_para_update.nome}): ")
    novo_nascimento = input(f"Nova data de nascimento (Atual: {estudante_para_update.nascimento}): ")
    novo_ra = input(f"Novo R.A (Atual: {estudante_para_update.ra}): ")
    novo_curso = input(f"Novo curso do estudante (Atual: {estudante_para_update.curso}): ")
    nova_logradouro = input(f"Novo logradouro do estudante(Atual: {estudante_para_update.endereco.logradouro}): ")
    nova_numero = input(f"Novo numero do estudante(Atual: {estudante_para_update.endereco.numero}): ")
    nova_cidade = input(f"Nova cidade do estudante(Atual: {estudante_para_update.endereco.cidade}): ")
    nova_estado = input(f"Novo estado do estudante(Atual: {estudante_para_update.endereco.estado}): ")

    if novo_nome.strip():
        estudante_para_update.nome = novo_nome
    if novo_nascimento.strip():
        estudante_para_update.nascimento = novo_nascimento
    if novo_ra.strip():
        estudante_para_update.ra = novo_ra
    if novo_curso.strip():
        estudante_para_update.curso = novo_curso
    if nova_logradouro.strip():
        estudante_para_update.endereco.logradouro = nova_logradouro
    if nova_numero.strip():
        estudante_para_update.endereco.numero = int(nova_numero)
    if nova_cidade.strip():
        estudante_para_update.endereco.cidade = nova_cidade
    if nova_estado.strip():
        estudante_para_update.endereco.estado = nova_estado

    print(f"\nDados do cliente '{ra_busca}' atualizados com sucesso!")


def excluir_estudante(lista_estudante):
    if lista_branco(lista_estudante):
        return

    mostrar_todos_aluno(lista_estudante)
    try:
        ra_busca = int(input("Digite o R.A do estudante que deseja excluir: "))
    except ValueError:
        print("R.A inválido.")
        return
    estudante_para_excluir = encontrar_aluno(lista_estudante, ra_busca)

    if estudante_para_excluir is None:
        print("\nEstudante não encontrado.")
        return

    lista_estudante.remove(estudante_para_excluir)
    print(f"\nEstudante com R.A '{ra_busca}' excluído com sucesso!")
 

while True:

    print("\nMenu de opções:")
    print("1. Adicionar estudante")
    print("2. Atualizar estudante")
    print("3. Excluir estudante")
    print("4. Mostrar todos os estudantes")
    print("5. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == '1':
        adicionar(lista_estudante)
    elif escolha == '2':
        atualizar_estudante(lista_estudante)
    elif escolha == '3':
        excluir_estudante(lista_estudante)
    elif escolha == '4':
        mostrar_todos_aluno(lista_estudante)
    elif escolha == '5':
        print("Saindo do programa...")
        time.sleep(1)
        break
    else:
        print("Opção inválida. Tente novamente.")

    time.sleep(4)
    os.system("cls || clear")