import os

# Lista que armazena todos os clientes
lista_de_clientes = [
    {
        "nome": "Ana Silva",
        "idade": 28,
        "email": "ana.silva@example.com",
        "celular": "(11) 98765-4321"
    },
    {
        "nome": "Bruno Souza",
        "idade": 35,
        "email": "bruno.souza@example.com",
        "celular": "(21) 99876-1234"
    },
    {
        "nome": "Carla Mendes",
        "idade": 24,
        "email": "carla.mendes@example.com",
        "celular": "(31) 91234-5678"
    },
    {
        "nome": "Diego Rocha",
        "idade": 42,
        "email": "diego.rocha@example.com",
        "celular": "(41) 98712-3456"
    },
    {
        "nome": "Eduarda Lima",
        "idade": 30,
        "email": "eduarda.lima@example.com",
        "celular": "(51) 98123-9876"
    }
]

# Função que limpa a tela
def limpar_tela():
    os.system("cls")

# Função que exibi o menu na tela
def exibir_menu():
    print("\n=== Menu Principal===")
    print(" [1] - Cadastro de Clientes.")
    print(" [2] - Listar Clientes Cadastrados.")
    print(" [3] - Editar Dados de Clientes.")
    print(" [4] - Excluir um Clientes.")
    print(" [5] - Sair do Sistema. \n")

# Função que volta para o menu principal
def voltar_ao_menu_principal():
    input("\nPessione <Enter> para voltar ao menu inicial..")
    main()

# Função que cadastar um novo cliente
def cadastrar_novo_cliente():
    try:
        # Chamar a função que limpa a tela
        limpar_tela()
        print("=== Cadastro de Novo Cliente ===")

        # Solicitando os dados do cliente
        nome = input("Digite o nome do cliente: ")
        idade = int(input("Digite a idade do cliente: "))
        email = input("Digite o e-mail do cliente: ")
        celular = input("Digite o celular do cliente: ")

        # Agrupando os dados do cliente
        dados_cliente = {
            'nome': nome,
            'idade': idade,
            'email': email,
            'celular': celular
        }

        # Adicionar o cliente na lista
        lista_de_clientes.append(dados_cliente)

        # Exibindo mensagem de sucesso
        print(f"\nO Cliente {nome} foi cadastrado com sucesso.!")

    except:
        print("A idade deve ser um número")

    finally:
        # Voltar para o menu principal
        voltar_ao_menu_principal()
    

# Função que lista todos os cliente cadastrados
def listar_clientes_cadastrados():
    # Chamar a função que limpa a tela
    limpar_tela()
    print("=== Lista de Clientes Cadastrados ===\n")

    # Listando os clientes
    for cliente in lista_de_clientes:
        print(f"Nome: {cliente['nome']} | Idade: {cliente['idade']} | E-mail: {cliente['email']} | Celular: {cliente['celular']}")

    # Volta para o menu principal
    voltar_ao_menu_principal()

# Função que exclui um cliente cadastrados
def excluir_cliente():
    # Chamar a função que limpa a tela
    limpar_tela()
    print("=== Remover Cliente ===\n")

    # Listando os clientes cadastrados
    for indice, cliente in enumerate(lista_de_clientes):
        print(f"Indíce: {indice} | Nome: {cliente['nome']} | Idade: {cliente['idade']} | E-mail: {cliente['email']} | Celular: {cliente['celular']}")
    try:

        # Solicitar ao usuario o indice para remover
        indice = int(input("\nDigite o indíce do cliente que deseja remover: "))
        
        if indice >= 0 and indice < len(lista_de_clientes):
            # Excluir o cliente escolhido
            cliente_removido = lista_de_clientes.pop(indice)

            print(f"\nO Cliente {cliente_removido['nome']} removido com sucesso..!")
        
        else:
            print("Índice Inválido")
        
    except:
        print("Digite um indice válido")

    finally:
        # Voltar ao menu principal
        voltar_ao_menu_principal()

def  editar_dados_cliente():
    # Chamar a função que limpa a tela
    limpar_tela()
    print("=== Editar Dados do Cliente === \n")

# Listando os clientes cadastrados
    for indice, cliente in enumerate(lista_de_clientes):
        print(f"Indíce: {indice} | Nome: {cliente['nome']} | Idade: {cliente['idade']} | E-mail: {cliente['email']} | Celular: {cliente['celular']}")
    
    try:

        # Solicitar ao usuario o indice para remover
        indice = int(input("\nDigite o indíce do cliente que deseja editar: "))

        if indice >= 0 and indice < len (lista_de_clientes):

            # Capturar os dados do cliente selecionado
            dados_do_cliente = lista_de_clientes[indice]

            # Exibindo os dados do cliente selecionado
            print(f"\nEditando os dados do cliente: {dados_do_cliente['nome']}")

            # Solicitando os novos dados
            novo_nome = input(f"Digite o novo nome Atual-{dados_do_cliente['nome']}): ")
            novo_idade = input(f"Digite a nova idade (Atual-{dados_do_cliente['idade']}): ")
            novo_email = input(f"Digite o novo e-mail (Atual-{dados_do_cliente['email']}): ")
            novo_celular = input(f"Digite o novo celular (Atual{dados_do_cliente['celular']}): ")

            # Editar
            dados_do_cliente['nome'] = novo_nome
            dados_do_cliente['idade'] = novo_idade
            dados_do_cliente['email'] = novo_email
            dados_do_cliente['celular'] = novo_celular

            print("\nDados Atualizados com sucesso!!")

    except:
        print("Idade ou Indice devem ser válidos")

    finally:  
        # Voltar ao menu principal
        voltar_ao_menu_principal()

# Função principal do meu programa
def main():
    # Chamar a função que limpa a tela
    limpar_tela()
    print("Bem Vindo ao Gerenciador de Clientes..")
    
    # Chamar a função que exibi o menu
    exibir_menu()

    # Solicitando uma opção para o usuario
    opcao =int(input("Ecolha uma opção: "))

    # Verificando qual foi a opção escolhida
    if opcao == 1:
        # Abrir o cadastro de um novo cliente
        cadastrar_novo_cliente()

    elif opcao == 2:
        # Abrir a listagem de clientes cadastrados
        listar_clientes_cadastrados()

    elif opcao == 3:
        # Abrir a edição de clientes
        editar_dados_cliente()

    elif opcao == 4:
        # Abrir a exclusão de um cliente
        excluir_cliente()
    
    elif opcao == 5:
        input("Pressione <Enter> para encerrar o programa...")
        exit()
    
    else:
        print("Opção Inválida!")


# Chamando a função principal
main()