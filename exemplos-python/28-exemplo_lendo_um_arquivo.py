import os

os.system("cls")

print(" === LENDO DADOS DE UM ARQUIVO ===\n")

input("Pressione a tecla <Enter> para continuar...")

os.system("cls")

# Acessando o arquivo para ler os dados
with open("produtos.txt","r",encoding="utf-8") as arquivo:
    print("=== DADOS O ARQUIVO ===\n")

    # Utilizando o print e o read para exibir os dados
    # print(arquivo.read())

    # Lendo linha por linha do arquivo
    for linha in arquivo:
        print(f"Conteúdo da Linha:{linha.strip()}")

        
input("Pressione a tecla <Enter> para encerrar..")

