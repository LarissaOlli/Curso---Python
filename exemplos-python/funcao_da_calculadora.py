def somar(numero01,numero02):
    resultado = numero01 + numero02
    print(f" A Soma é: {resultado}")

def subtrair(numero01,numero02):
    resultado = numero01 - numero02
    print(f" A Subtração é: {resultado}")

def dividir(numero01,numero02):
    resultado = numero01 / numero02
    print(f"A divisão é: {resultado}")

def multiplicar(numero01,numero02):
    resultado = numero01 * numero02
    print(f"A Multiplicação é: {resultado}")

def calcular_resto_divisao(numero01,numero02):
    resultado = numero01 % numero02
    print(f"O RESTO da divisão é: {resultado}")

def imprimir_msg_erro():
    print("Opção Inválida..!!")

def somar_com_retorno(numero01,numero02):
    resultado = numero01 + numero02
    return resultado

def subtrair_com_retorno(numero01,numero02):
    resultado = numero01 - numero02
    return resultado

def exibir_menu():
    print("===========================================")
    print("Selecione uma opção abaixo")
    print("[1] - Soma")
    print("[2] - Subtração")
    print("[3] - Divisão")
    print("[4] - Multiplicação")
    print("[5] - O RESTO DA DIVISÃO")