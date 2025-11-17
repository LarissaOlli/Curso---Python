programa {
  funcao inicio() {
    
    //1 Passo - Declarar as variaves
    cadeia nome
    real nota01
    real nota02
    real nota03
    real media

    //2 Passo - Entradade de dados
    escreva (" Digite o seu nome:")
    leia(nome)

    escreva(" Digite sua primeira nota:")
    leia(nota01)

    escreva(" Digite sua segunda nota:")
    leia(nota02)

    escreva(" Digite sua terceira nota:")
    leia(nota03)

    //3 Passo - Processamento
    media = (nota01 + nota02 + nota03) / 3

    //4 Passo - Saída
    escreva("Sua média é:", media)

  }
}
