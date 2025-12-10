#importando a biblioteca os
import os

#limpando a tela
os.system("cls")

print("""
     
██████╗░░█████╗░██╗░░░░░███████╗████████╗██╗███╗░░░███╗
██╔══██╗██╔══██╗██║░░░░░██╔════╝╚══██╔══╝██║████╗░████║
██████╦╝██║░░██║██║░░░░░█████╗░░░░░██║░░░██║██╔████╔██║
██╔══██╗██║░░██║██║░░░░░██╔══╝░░░░░██║░░░██║██║╚██╔╝██║
██████╦╝╚█████╔╝███████╗███████╗░░░██║░░░██║██║░╚═╝░██║
╚═════╝░░╚════╝░╚══════╝╚══════╝░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝
      """)

resposta = "sim"

while (resposta == "sim"):

    nome = input("Digite seu nome: ")
    nota01 = float (input("Digite sua primeira nota: "))
    nota02 = float (input("Digite sua segunda nota: "))
    nota03 = float (input("Digite sua terceira nota: "))

    media = (nota01 + nota02 + nota03) / 3

    situaçao_do_aluno = ""

    print(f"Sua média foi {round(media,2)}")


    if media >=7:
        print("Aprovado")
        situaçao_do_aluno = "Aprovado"
        
    elif media >4:
        print ("Em recuperação")
        situaçao_do_aluno = "Recuperação"

    else:
        print("Reprovado")
        situaçao_do_aluno = "Reprovado"

    # Gravar os dados dos alunos
    with open("notas_dos_alunos.txt","a",encoding="utf-8") as arquivo:
        arquivo.write(f"Nome do Aluno: {nome} \n")
        arquivo.write(f"Nota 01: {nota01}\n")
        arquivo.write(f"Nota 02: {nota02}\n")
        arquivo.write(f"Nota 03: {nota03}\n")
        arquivo.write(f"Média do Aluno: {media}\n")
        arquivo.write(f"Situação do Aluno: {situaçao_do_aluno}\n")
        arquivo.write("========================================================= \n")

        print("Dados salvos com sucesso!!")
    
    resposta = input("Gostaria de executar novamente, sim ou não?: ")
    
    os.system("cls")

input("Pressione qualquer <Enter> para fechar o programa.") 
      
