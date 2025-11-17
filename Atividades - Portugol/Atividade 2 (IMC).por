programa {
  funcao inicio() {
    //1 Passo - Declarar as variaveis
    real numero1
    real numero2
    real multiplicacao
    real divisao
    real subtracao

    // 2 Passo - Entrada
    escreva("Digite o primeiro numero: ")
    leia(numero1)

    escreva(" Digite o segundo numero: ")
    leia(numero2)

    // 3 Passo - Processamento
    multiplicacao = numero1 * numero2
    divisao = numero1 / numero2
    subtracao = numero1 - numero2

    // 4 Passo - Saída
    escreva("A Multiplicação é: ", multiplicacao)
    escreva("\nA Divisão é: ", divisao)
    escreva("\nA Subtração é: ",subtracao)

    

  }
}
