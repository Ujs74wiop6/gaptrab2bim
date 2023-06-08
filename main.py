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
#MODULO 2 -> PRODUTO
#MODULO 3 -> COMPRA
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