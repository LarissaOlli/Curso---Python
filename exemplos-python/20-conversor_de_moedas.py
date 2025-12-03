import os


# Função qe exibi o menu
def exibir_menu():
    print("\n === CONVERSOR DE MOEDAS ===")
    print("[1] Converter DOlAR -> REAL")
    print("[2] Converter REAL -> DOLAR")
    print("[0] Sair")

# Função converter de dolar para real
def converter_dolar_para_real(quantia_dolar, taxa):
    return quantia_dolar * taxa

# Função converter de real para dolar
def converter_real_para_dolar(quantia_real, taxa):
    return quantia_real / taxa

# Função principal do programa
def main():
   os.system("cls")
   
   # Solicitando a ataxa de cambio do dia
   taxa_cambio = float(input("Informe a taxa de câmbio" "(1 USD = quantos BRL?):"))

   resposta = "sim"

   while resposta == "sim":
        # Limpando a tela
        os.system("cls")
        
        #Chamando a função exibir_menu
        exibir_menu()

        # Solicitando a opção do usuário
        opcao = input("Escolha uma opção: ")

        # Verificando a opção escolhida
        if opcao =="1":
           quantia_dolar = float(input("Digite a quantia em DOLAR (USD): "))
           total_convertido = converter_dolar_para_real(quantia_dolar,taxa_cambio)
           print(f"USD {quantia_dolar} = R$ {total_convertido}")

        elif opcao == "2":
            quantia_real = float(input("Digite a quantia em REAL (BRL): "))
            total_convertido = converter_real_para_dolar(quantia_real, taxa_cambio)
            print(f"R$ {quantia_real} -> USD {total_convertido}")

        elif opcao == "0":
            print("Encerrando o programa...Até mais!")
            break

        else:
            print("Opção invalida! Tente Novamente!")

        resposta = input("Deseja realizar outra conversão? (sim/não)")



# Chamando a função main
main() 