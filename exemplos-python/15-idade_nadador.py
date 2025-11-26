#importando a biblioteca os
import os

#limpando a tela
os.system("cls")

print("Atividade 03 - Classificação de Nadador")
idade = int(input("Digite a idade do nadador:"))

#Infantil A - 5 a 7 anos.
if idade >=5 and idade <=7:
    print("Infantil A")

elif idade >=8 and idade <=11:
    print("Infantil B")

elif idade >=12 and idade <=13:
    print("Juvenil A")

elif idade >=14 and idade <=17:
    print("Juvenil B")

elif idade >=18:
    print("Adultos")

else:
    print("A idade Inválida!")

input("Pressione a tecla <Enter> para finalizar")