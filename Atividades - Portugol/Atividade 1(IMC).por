programa {
  
  inclua biblioteca Matematica--> mat
  
  funcao inicio() {

//1 Passo - Declarar as variaveis
real peso
real altura
real imc

//2 Passo - Entrada
escreva ("Digite seu peso:")
leia (peso)

escreva ("Digite sua altura:")
leia(altura)

//3 Passo - Processamento
imc = peso / (altura * altura)

//4 Passo - Saída
escreva("Seu IMC é: ", mat.arredondar(imc,2))

  }
}
