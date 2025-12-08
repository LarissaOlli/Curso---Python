import os

os.system("cls")

print("Exemplos de Tratamento de Excecões")

try:

    comando = "print('teste')"

    exec(comando)
    

    numero01 = int(input("Digite o primeiro número: "))
    numero02 = int(input("Digite o segundo número: "))
    
    resultado = numero01 / numero02
    print(f"O Resultado da divisão é: {resultado}")

except Exception as erro:
    print(f"Aconteceu o erro {erro}")
    print("Você digitou um valor ínvalido!")



