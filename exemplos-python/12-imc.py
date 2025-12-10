#importando a biblioteca os
import os

#limpando a tela
os.system("cls")

resposta = "sim"

while (resposta =="sim"):

    nome = input("Digite seu nome: ")
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))

    imc = peso / (altura * altura)

    imc_dos_pacientes = ""

    print(f"Olá {nome}, seu IMC é: {round(imc,2)}")


    if imc <=18.5:
        print("Você está abaixo do peso.")
        imc_dos_pacientes = "Você está abaixo do peso."

    elif imc >=24.9:
        print("Peso normal.")
        imc_dos_pacientes = "Peso normal."

    elif imc <=29.9:
        print("Sobrepeso.")
        imc_dos_pacientes = "Sobrepeso."

    elif imc <=34.9:
        print("Obesidade grau I") 
        imc_dos_pacientes = "Obesidade grau I"

    elif imc <=39.9:
        print("Obesidade grau II")
        imc_dos_pacientes = "Obesidade grau II"

    elif imc >=40:
        print("Obessidade grau III")
        imc_dos_pacientes = "Obessidade grau III"
    
    with open("imc_dos_pacientes.txt","a",encoding="utf-8") as arquivo:
        arquivo.write(f"Nome do Paciente: {nome} \n")
        arquivo.write(f"Peso do Paciente: {peso}\n")
        arquivo.write(f"Altura do Paciente: {altura}\n")
        arquivo.write(f"Olá {nome}, seu IMC é: {imc_dos_pacientes}\n")
        arquivo.write("========================================================= \n")

        print("IMC feito com sucesso!!")
    
    resposta = input("Gostaria de executar novamente, sim ou não?: ")
    
    os.system("cls")
   

input("Pressione <Enter> para fechar o programa")

