import os

os.system("cls")

print("Exemplo com While - Salário do Professor")

resposta = "sim"

while (resposta == "sim"):
    os.system("cls")

    print("Qual é o seu Nível: \n 1- Nível 1 \n 2- Nível 2 \n 3- Nível 3")

    nivel = input("Informe o seu Nível: ")

    qtd_aulas = int(input("Qual é sua qtd de aulas por semana: "))

    if nivel == "1":
        salario = (qtd_aulas * 12) * 4

    elif nivel == "2":
        salario = (qtd_aulas * 17) * 4

    elif nivel == "3":
        salario = (qtd_aulas * 25) * 4

    else:
        print("O nível digitado é invalido!")

    print(f"O seu salário será: {salario}")

    resposta = input("Deseja executar novamente? (Sim ou Não): ").lower()

input("Pressionea tecla <Enter> para finalizar..")


