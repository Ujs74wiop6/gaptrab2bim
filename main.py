import os

#---------------------------------------------------------
#
# Sistema Simples para manipulação de registros em Matriz 
#
#  --------------------------------------------------------
# 
# 'CRUD' -> Cadastro, Listagem, Edição e Remoção
#
#  --------------------------------------------------------
#
# Entidades: 
#   [CLIENTE],[PRODUTO],[COMPRA]
#
#  --------------------------------------------------------
# 
# IFSP - Votuporanga
# Sistemas de Informação | 2023
# Metétia: [GAPS3] GESTÃO ÁGIL DE PROJETOS 
# Professor: Evandro Jardini 
# Alunos: Fabricio Tiago Arantes e Evelyn Nayara Amaral


#MODULO 1 -> CLIENTE
class Cliente:
    def __init__(self, cpf_cliente, nome_cliente):
        self.cpf_cliente = cpf_cliente
        self.nome_cliente = nome_cliente

clientes = []

def criar_clientes():
    cpf_cliente = input("Digite o CPF do cliente: ")
    nome_cliente = input("Digite o nome do cliente: ")
    cliente = Cliente(cpf_cliente, nome_cliente)
    clientes.append(cliente)
    print("Cliente criado com sucesso!")

def listar_clientes():
    print("CLIENTES:")
    for cliente in clientes:
        print(f"\n | CPF: {cliente.cpf_cliente} | NOME: {cliente.nome_cliente} | ")
        print("-")

def atualizar_clientes():
    cpf_cliente = input("Digite o CPF do cliente que deseja atualizar: ")
    cliente = next((c for c in clientes if c.cpf_cliente == cpf_cliente), None)
    if cliente is None:
        print("Cliente não encontrado.")
        return
    novo_nome = input("Digite o novo nome do cliente: ")
    cliente.nome_cliente = novo_nome
    print("Cliente atualizado com sucesso!")

def deletar_cliente():
    cpf_cliente = input("Digite o CPF do cliente que deseja deletar: ")
    cliente = next((c for c in clientes if c.cpf_cliente == cpf_cliente), None)
    if cliente is None:
        print("Cliente não encontrado.")
        return
    clientes.remove(cliente)
    print("Cliente deletado com sucesso!")


#MODULO 2 -> PRODUTO
class Produto:
    def __init__(self, cod_produto, nome_produto, valor_produto):
        self.cod_produto = cod_produto
        self.nome_produto = nome_produto
        self.valor_produto = valor_produto

produtos = []

def criar_produtos():
    cod_produto = input("Digite o código do produto: ")
    nome_produto = input("Digite o nome do produto: ")
    valor_produto = float(input("Digite o valor do produto: "))
    produto = Produto(cod_produto, nome_produto, valor_produto)
    produtos.append(produto)
    print("Produto criado com sucesso!")

def listar_produtos():
    print("PRODUTOS:")
    for produto in produtos:
        print(f"\n | CÓDIGO: {produto.cod_produto} | NOME: {produto.nome_produto} | VALOR: {produto.valor_produto} | ")
        print("-")

def atualizar_produtos():
    cod_produto = input("Digite o código do produto que deseja atualizar: ")
    produto = next((p for p in produtos if p.cod_produto == cod_produto), None)
    if produto is None:
        print("Produto não encontrado.")
        return
    
    nome_or_value = input("1 - Modficar o Nome do Produro\n2 - Modificar o Preco do Produto\n: ")

    if nome_or_value == '1':
        novo_nome = input("Digite o novo nome do Produto: ")
        produto.nome_produto = novo_nome
        print("Nome do Produto atualizado com sucesso!")
    elif nome_or_value == '2':
        novo_valor = float(input("Digite o novo valor do produto: "))
        produto.valor_produto = novo_valor
        print("Valor do Produto atualizado com sucesso!")

def deletar_produto():
    cod_produto = input("Digite o código do produto que deseja deletar: ")
    produto = next((p for p in produtos if p.cod_produto == cod_produto), None)
    if produto is None:
        print("Produto não encontrado.")
        return
    produtos.remove(produto)
    print("Produto deletado com sucesso!")



#MODULO 3 -> COMPRA
class Compra:
    def __init__(self, cliente, produto, qtd):
        self.cliente = cliente
        self.produto = produto
        self.qtd = qtd
        self.valor_final = self.produto.valor_produto * self.qtd

compras = []

def criar_compras():
    cpf_cliente = input("Digite o CPF do cliente: ")
    cod_produto = input("Digite o código do produto: ")
    qtd = int(input("Digite a quantidade: "))
    
    cliente = next((c for c in clientes if c.cpf_cliente == cpf_cliente), None)
    produto = next((p for p in produtos if p.cod_produto == cod_produto), None)
    
    if cliente is None or produto is None:
        print("Cliente ou produto não encontrado.")
        return
    
    compra = Compra(cliente, produto, qtd)
    compras.append(compra)
    print("Compra criada com sucesso!")

def listar_compras():
    print("COMPRAS:")
    for compra in compras:
        print(f"\n | CLIENTE: {compra.cliente.nome_cliente} | PRODUTO: {compra.produto.nome_produto} | QUANTIDADE: {compra.qtd} | VALOR FINAL: {compra.valor_final} | ")
        print("-")

def atualizar_compras():
    cpf_cliente = input("Digite o CPF do cliente da compra que deseja atualizar: ")
    cod_produto = input("Digite o código do produto da compra que deseja atualizar: ")
    compra = next((c for c in compras if c.cliente.cpf_cliente == cpf_cliente and c.produto.cod_produto == cod_produto), None)
    if compra is None:
        print("Compra não encontrada.")
        return
    nova_qtd = int(input("Digite a nova quantidade: "))
    compra.qtd = nova_qtd
    compra.valor_final = compra.produto.valor_produto * compra.qtd
    print("Compra atualizada com sucesso!")

def deletar_compra():
    cpf_cliente = input("Digite o CPF do cliente da compra que deseja deletar: ")
    cod_produto = input("Digite o código do produto da compra que deseja deletar: ")
    compra = next((c for c in compras if c.cliente.cpf_cliente == cpf_cliente and c.produto.cod_produto == cod_produto), None)
    if compra is None:
        print("Compra não encontrada.")
        return
    compras.remove(compra)
    print("Compra deletada com sucesso!")

# MENU PRINCIPAL - SISTEMA

while True:
    print("\nEscolha a matriz que deseja acessar:")
    print("1. Cliente")
    print("2. Produto")
    print("3. Compra")
    print("0. Sair")

    escolha = input("Digite o número correspondente: ")

    if escolha == '0':
        break

    elif escolha == '1':
        opc = input("Oque deseja realizar com o CLIENTE\n1 - Criar\n2 - Listar\n3 - Atualizar\n4 - Remover\n: ")
        if opc == '1':
            criar_clientes()
        elif opc == '2':
            os.system('clear')
            listar_clientes()
        elif opc == '3':
            atualizar_clientes()
        elif opc == '4':
            deletar_cliente()

    elif escolha == '2':
        opc = input("Oque deseja realizar com o PRODUTO\n1 - Criar\n2 - Listar\n3 - Atualizar\n4 - Remover\n: ")
        if opc == '1':
            criar_produtos()
        elif opc == '2':
            os.system('clear')
            listar_produtos()
        elif opc == '3':
            atualizar_produtos()
        elif opc == '4':
            deletar_produto()

    elif escolha == '3':
        opc = input("Oque deseja realizar com a COMPRA\n1 - Criar\n2 - Listar\n3 - Atualizar\n4 - Remover\n: ")
        if opc == '1':
            criar_compras()
        elif opc == '2':
            os.system('clear')
            listar_compras()
        elif opc == '3':
            atualizar_compras()
        elif opc == '4':
            deletar_compra()
    else:
        print("Escolha inválida!")
        continue