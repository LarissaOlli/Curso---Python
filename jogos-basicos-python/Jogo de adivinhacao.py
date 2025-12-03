import os

os.system("cls")

import random

resposta = "sim"

while resposta == "sim":
 
    os.system("cls")

    # Computador escolhe um número
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 5


    print("""
    ╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╭━━━╮╱╭╮╱╱╱╱╱╱╱╭╮
    ╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱┃╭━╮┃╱┃┃╱╱╱╱╱╱╱┃┃
    ╱╱┃┣━━┳━━┳━━╮╭━╯┣━━╮┃┃╱┃┣━╯┣┳╮╭┳┳━╮┃╰━┳━━┳━━┳━━┳━━╮
    ╭╮┃┃╭╮┃╭╮┃╭╮┃┃╭╮┃┃━┫┃╰━╯┃╭╮┣┫╰╯┣┫╭╮┫╭╮┃╭╮┃╭━┫╭╮┃╭╮┃
    ┃╰╯┃╰╯┃╰╯┃╰╯┃┃╰╯┃┃━┫┃╭━╮┃╰╯┃┣╮╭┫┃┃┃┃┃┃┃╭╮┃╰━┫╭╮┃╰╯┃
    ╰━━┻━━┻━╮┣━━╯╰━━┻━━╯╰╯╱╰┻━━┻╯╰╯╰┻╯╰┻╯╰┻╯╰┻━━┻╯╰┻━━╯
    ╱╱╱╱╱╱╭━╯┃
    ╱╱╱╱╱╱╰━━╯""")
    print(f"Tente adivinhar o número entre 1 e 100")
    print(F"Você tem {max_tentativas} tentativas.")

    while tentativas < max_tentativas:
        tentativas += 1
        tentativas_restantes = max_tentativas - tentativas

        # Solicita um palpite
        try:
            palpite = int(input(f"\ntentativas {tentativas}: "))
        except ValueError:
            print("Por Favor, digite apenas números!!")
            continue

        # Verifica o palpite
        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativas..!")
            break

        elif palpite < numero_secreto:
            print(f"Muito baixo! Tente novamente, um número maior.")
            if tentativas_restantes > 0:
                print(f"Restam {tentativas_restantes} tentativas.")

        else:
            print(f"Muito Alto! Tente novamente, um número menor.")
            if tentativas_restantes > 0:
                print(f"Restam {tentativas_restantes} tentativas.")

        # Dica de tentativas
        if tentativas == max_tentativas // 3:
            if numero_secreto <= 30:
                print("Dica rapida: O número está na primeira metade (1 - 30)")
            elif numero_secreto >= 31:
                print("Dica rapida: O número está na segunda metade (31 - 70)")
            else:
                print("Dica rapida: O número está na terceira metade (71 - 100)") 

        if tentativas == max_tentativas:
            print(f"\nVocê perdeu!! O número era {numero_secreto}")
    resposta = input("Deseja jogar novamente? (sim ou não): ").lower()
input("Pressione a tecla <Enter> para finalizar o jogo..")
