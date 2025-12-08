import os

os.system("cls")

try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero

except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")

except ValueError:
    print("Erro: você não digitou um número válido.")

else:
    # Executa apenas se ** nenhuma exceção ** tiver ocorrido
    print(f"O resultado da divisão é: {resultado}")
finally:
    # Executa sempre, independente de rro ou sucesso
    print("Encerrando a operção...")