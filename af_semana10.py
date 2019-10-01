#!/usr/bin/python3
#coding: utf-8

# Exercicio 1
# Faça um algoritmo que solicite ao usuário números e os armazene em um vetor de 30 posições. Crie uma função que recebe o vetor preenchido e substitua todas as ocorrências de valores positivos por 1 e as de valores negativos por 0.
def exercicio1():
    vetor = []
    # Adicionar os vcalores digitados pelo usuario para o vetor
    for i in range(0, 30):
        num = int(input('Digite um numero a ser adicionado no vetor:\n'))
        vetor.append(num)
    # Funcao que recebe o valorda posicao do vetor e verifica se o numero for maior que zero, recebe 1
    def modVetor(numero):
        modNumero = 0
        if (numero > 0):
            modNumero = 1
        return modNumero
    # Inicio da impressao do vetor modificado
    print('Vetor modificado:\n')
    for i in range(0, 30):
        vetor[i] = modVetor(vetor[i])
        print(vetor[i], end = ' ')
    print('\n')

# Exercicio 2
# Crie uma função que retorne o valor da expressão: 2/3 + 3/5 + 4/7 + 5/9 + … + n/m, para um valor de n definido pelo usuário. Verifique se esse valor de n é positivo e, caso não seja, solicite outro até ser fornecido um valor positivo.
def exercicio2():    
    # Recebe o numero de vezes que a funcao sera executada
    num = int(input('Digite o numero de vezes que a expressao deve ser executada:\n'))
    while (num <= 0):
        num = int(input('O numero deve ser positivo'))
    # Inicio da funcao que ira calcular a expressao
    def execExpressao(n):
        numero1 = 2
        numero2 = 3
        soma = 0
        while (numero1 <= n):
            soma += numero1 / numero2
            numero1 += 1
            numero2 += 2
        return soma
    # Imprime o resultado da soma das fracoes feita pela funcao
    print('O resultado da soma das fracoes da expressao e de {}\n'.format(execExpressao(num)))

# Menu de selecao das funcoes
escolha = 0
while escolha != 3:
    escolha = int(input('Digite qual funcao deseja executar:\n [1] Exercicio 1\n [2] Exercicio 2\n [3] Sair do programa\n'))
    if(escolha == 1):
        exercicio1()
    elif(escolha == 2):
        exercicio2()
# Fim do programa
