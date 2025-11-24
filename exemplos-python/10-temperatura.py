#importando a biblioteca os
import os

#limpando a tela
os.system("cls")

temperatura = float(input("Digite a temperatura em celsius: "))

if temperatura >= 30:
    print("Está quente!")

elif temperatura >= 20:
    print("Está agradável!")

elif temperatura >= 10:
    print("Está frio!")

else:
    print("Está muito frio!")