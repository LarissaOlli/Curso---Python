import os
import random

os.system("cls")

# Função que sorteia um número (a a 50)
def sortear_numero_secreto():
    numero_secreto = random.randint(1,50)
    return numero_secreto

# Fução que solicita um palpite
def solicitar_palpite():
    palpite = int(input("Digite seu palpite: "))
    return palpite

# Função que verificar o palpite do jogador
def verificar_palpite(palpite, numero_secreto):
    # Verificar se o palpite é menor que o numero-secreto
    if palpite < numero_secreto:
        return "Menor"
    
    elif palpite > numero_secreto:
        return "Maior"
    
    else:
        return "Igual"
    
# Função principal
def main():
    
    # Gera o número secreto
    numero_secreto = sortear_numero_secreto()

    # Controla o número de tentativas
    tentativas = 0

    print(" Bem Vindo ao jogo da adivanhação!")
    print("Tente adivinhar o número entre 1 e 50 \n")

    while tentativas <= 5:
       
        # Acrescentar o número de tentativas
        tentativas += 1

        # Solicitando um palpite
        palpite = solicitar_palpite()

        # Verificar o palpite do jogador
        resultado = verificar_palpite(palpite, numero_secreto)
        
        if resultado == "Menor":
            print("Seu palpite foi menor que o número secreto, Tente Novamente.!")

        elif resultado == "Maior":
            print("Seu palpite foi maior que o número secreto, Tente Novamente.!")

        else:
            print(f"Parabéns, você acertouu em {tentativas} tentativas..!!")
            break
    else:
        print("Fim de Jogo..!!")

        
# Chamar a função main
main()