#importando a biblioteca os
import os

#limpando a tela
os.system("cls")

print("Atividade 02 - Positivo ou Negativo")

numero = int(input("Digite um numero:"))

if numero >=0:
    print("O numero é positivo")

else:
    print("O numero é negativo")

input("Pressione a tecla <enter> para finalizar")
