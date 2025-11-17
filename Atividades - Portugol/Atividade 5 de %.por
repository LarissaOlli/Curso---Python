programa {
  funcao inicio() {
  // 1 Passo - Declarar as variaveis
  
  real valor 
  real porcentagem
  real resultado

  //  2 Passo - Entrada
  escreva(" Digite o valor: ")
  leia(valor)

  escreva(" Digite a porcentagem: ")
  leia(porcentagem)

  // 3 Passo - Processamento
 resultado = valor * (porcentagem/100)

  // 4 Passo - Saída
  escreva(" O valo correspondente a ", porcentagem, "% de ", valor, " é ", resultado)


  }
}
