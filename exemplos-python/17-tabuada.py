#importando a biblioteca os
import os

#limpando a tela
os.system("cls")

print("Exemplo - Calculando a Tabuada")

numero = int(input("Digite um número: "))

i = 10
while (i >=0):
    print(f"{numero} X {i} = {numero * i}")
    i-=1

print("O programa terminou")
input("Pressionea tecla <Enter> para finalizar..")


