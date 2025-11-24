#importando a biblioteca os
import os

#limpando a tela
os.system("cls")

print("Atividade - Par ou Ímpar")

numero = int(input("Digite um numero: "))

if numero % 2 == 0:
    print("O numero é PAR")

else:
    print("O numero é ÍMPAR")
