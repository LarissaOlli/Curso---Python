import os

os.system("cls")



# Importar as funções
import funcao_da_calculadora as funcoes

resposta = "sim"

while resposta == "sim":

    os.system("cls")

    print(""" 
            ╭━━━┳━━━┳╮╱╱╭━━━┳╮╱╭┳╮╱╱╭━━━┳━━━┳━━━┳━━━┳━━━╮
            ┃╭━╮┃╭━╮┃┃╱╱┃╭━╮┃┃╱┃┃┃╱╱┃╭━╮┣╮╭╮┃╭━╮┃╭━╮┃╭━╮┃
            ┃┃╱╰┫┃╱┃┃┃╱╱┃┃╱╰┫┃╱┃┃┃╱╱┃┃╱┃┃┃┃┃┃┃╱┃┃╰━╯┃┃╱┃┃
            ┃┃╱╭┫╰━╯┃┃╱╭┫┃╱╭┫┃╱┃┃┃╱╭┫╰━╯┃┃┃┃┃┃╱┃┃╭╮╭┫╰━╯┃
            ┃╰━╯┃╭━╮┃╰━╯┃╰━╯┃╰━╯┃╰━╯┃╭━╮┣╯╰╯┃╰━╯┃┃┃╰┫╭━╮┃
            ╰━━━┻╯╱╰┻━━━┻━━━┻━━━┻━━━┻╯╱╰┻━━━┻━━━┻╯╰━┻╯╱╰╯""")


    numero01 = float(input("Digite o primeiro numero: "))
    numero02 = float(input("Digite o segundo numero: "))
    
    funcoes.exibir_menu()

    opcao = input("Escolha uma Opção: ")

    if opcao == "1":
        print(f"A soma é: {funcoes.somar_com_retorno(numero01,numero02)}")

    elif opcao == "2":
        print(f"A sub é: {funcoes.subtrair_com_retorno(numero01,numero02)}")

    elif opcao == "3":
        funcoes.dividir(numero01,numero02)

    elif opcao == "4":
        funcoes.multiplicar(numero01,numero02)

    elif opcao =="5":
        funcoes.calcular_resto_divisao(numero01,numero02)

    else:
        funcoes.imprimir_msg_erro()

    resposta = input("Deseja executar novamente? (Sim ou Não): ").lower()

print("Programa encerrado com sucesso!!")
