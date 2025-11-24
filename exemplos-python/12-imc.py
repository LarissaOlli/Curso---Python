#importando a biblioteca os
import os

#limpando a tela
os.system("cls")

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

print(f"Olá {nome}, seu IMC é: {round(imc,2)}")


if imc <=18.5:
    print("Você está abaixo do peso.")

elif imc >=24.9:
    print("Peso normal.")

elif imc <=29.9:
    print("Sobrepeso.")

elif imc <=34.9:
    print("Obesidade grau I") 

elif imc <=39.9:
    print("Obesidade grau II")

elif imc >=40:
    print("Obessidade grau III")

input("Pressione <Enter> para fechar o programa")
