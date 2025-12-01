import os

#Limpando a tela
os.system("cls")

#Exemplo de função sem parametros
def escreva():
    print("Bem vindo ao sistema")

#Exemplo de função com parametros
def exibir_idade(suaidade, nome):
    print(f" Seu nome é {nome}, você tem {suaidade} anos!")

def somar(n1,n2):
    resultado = n1 + n2
    print(f"O resultado é: {resultado}")

# Exemplo de função com retorno
def subtrair(valor1,valor2):
    resultado = valor1 - valor2
    return resultado
    
print("Executou o programa")

# chamando uma funcao sem parametros
escreva()

# chamando uma funcao sem parametros
exibir_idade(17,"Geovanna")
exibir_idade(26, "Larissa")
somar(50,90)

# Chamando uma função com retorno
print(f"A subtração é: {subtrair(5,2)}")