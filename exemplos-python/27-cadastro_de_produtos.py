import os

os.system("cls")

print("=== SALVANDO DADOS DO PRODUTO EM UM ARQUIVO ===")

nome_produto = input("Digite o nome do produto: ")
fabricante = input("Digite o fabricante: ")
categoria = input("Digite a categoria: ")
preco = float(input("Digite o preço do produto: "))

# Manipulando arquivo
arquivo = open("produtos.txt","a",encoding="utf-8")

# Gravando as informações dentro do arquivo
arquivo.write(f"Produto:{nome_produto} | Fabricante:{fabricante} | Categoria:{categoria} | Preço:{preco:.2f}\n")

# Fachar o arquivo
arquivo.close()

input("Pressione a tecla <Enter> para encerrar...")
