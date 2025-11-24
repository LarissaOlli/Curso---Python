#importando a biblioteca os
import os

#limpando a tela
os.system("cls")

print("""
     
██████╗░░█████╗░██╗░░░░░███████╗████████╗██╗███╗░░░███╗
██╔══██╗██╔══██╗██║░░░░░██╔════╝╚══██╔══╝██║████╗░████║
██████╦╝██║░░██║██║░░░░░█████╗░░░░░██║░░░██║██╔████╔██║
██╔══██╗██║░░██║██║░░░░░██╔══╝░░░░░██║░░░██║██║╚██╔╝██║
██████╦╝╚█████╔╝███████╗███████╗░░░██║░░░██║██║░╚═╝░██║
╚═════╝░░╚════╝░╚══════╝╚══════╝░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝
      """)

nome = input("Digite seu nome: ")
nota01 = float (input("Digite sua primeira nota: "))
nota02 = float (input("Digite sua segunda nota: "))
nota03 = float (input("Digite sua terceira nota: "))

media = (nota01 + nota02 + nota03) / 3

print(f"Sua média foi {round(media,2)}")


if media >=7:
    print("Aprovado")
    
elif media >4:
    print ("Em recuperação")

else:
    print("Reprovado")

input("Pressione qualquer <Enter> para fechar o programa.")    

      