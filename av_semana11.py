#!/usr/bin/python3
#coding: utf-8

# Inicio do exercício 1
# Dada uma sequência de números inteiros maiores que 1, terminando por 0, determine quantos números primos há nela. Crie uma função car para determinar os números primos.
def exercicio1():
    vetorNum = []
    num = 1
    # Recebe os numeros digitados pelo usuario e os adiciona em um vetor
    while (num != 0):
        num = int(input('Digite um numero inteiro positivo e maior que 1 ou digite 0 (zero) para sair:\n'))
        if (num > 1):
            vetorNum.append(num)
        else:
            print('O numero precisa ser positivo e maior que 1\n')
    # Funcao que checa se o numero e primo ou nao
    # Não consegui fazer apenas com uma função, o unico jeito de fazer corretamente, foi fazer a verificacao do número em separado
    def checkPrimo(numero):
        numDiv = 0
        for i in range(2, numero + 1):
            if (numero % i == 0):
                numDiv += 1
        if(numDiv > 1):
            return False
        else:
            return True
    # Função que faz o loop no vetor e checa os números usando a outra função
    def car(vetor):
        vetorResultado = []
        numDiv = 0
        for i in range(0, len(vetor)):
            if (checkPrimo(vetor[i])):
                vetorResultado.append(vetor[i])
        return vetorResultado
    # Início da impressão do vetor original, como digitado pelo usuário
    print('Os numeros digitados sao:\n{}'.format(vetorNum))
    # Início da impressão do vetor modificado
    print('Os numeros primos contidos na sequencia de numeros digitados sao:\n{}'.format(car(vetorNum)))

# Início do exercício 2
# Faça um algoritmo que solicite ao usuário números e os armazene em um vetor de 20 posições. Crie uma função que receba o vetor preenchido e substitua todas as ocorrências de valores negativos por 0, as de valores menores do que 10 por 1 e as demais por 2.
def exercicio2():
    vetor = []
    # Adicionar os valores digitados pelo usuario para o vetor
    for i in range(0, 20):
        num = int(input('Digite um numero a ser adicionado no vetor:\n'))
        vetor.append(num)
    # Funcao que recebe o valor da posicao do vetor e verifica se o numero for maior que zero, recebe 1
    def modVetor(numero):
        modNumero = 0
        if (numero > 0 and numero < 10):
            modNumero = 1
        elif (numero >= 10):
            modNumero = 2
        return modNumero
    # Inicio da impressao do vetor como foi digitado
    print('O vetor como foi digitado:\n{}\n'.format(vetor))
    # Inicio da impressao do vetor modificado
    print('O vetor depois de modificado:\n')
    for i in range(0, 20):
        vetor[i] = modVetor(vetor[i])
        print(vetor[i], end = ' ')
    print('\n')

# Início do exercício 3
# Crie um algoritmo que solicite 3 valores que representarão os lados de um triângulo. Considere que não importa a ordem em que serão fornecidos os valores, podendo ser fornecido primeiramente a hipotenusa e depois os catetos ou os catetos e depois a hipotenusa etc. Crie também uma função que recebe o vetor e retorne se os lados informados formam um triângulo retângulo. Você pode utilizar o teorema de Pitágoras para auxiliar na resolução: hipotenusa2 = cateto12 + cateto22.
def exercicio3():
    vetorNum = []
    for i in range(0,3):
        vetorNum.append(int(input('Digite um dos lados do triângulo:\n')))
    def checkTriangulo(vetor):
        hipotenusa = 0
        cateto1 = 0
        cateto2 = 0
        if (vetor[0] > vetor[1] and vetor[0] > vetor[2]):
            hipotenusa = vetor[0]
            cateto1 = vetor[1]
            cateto2 = vetor[2]
        elif (vetor[1] > vetor[0] and vetor[1] > vetor[2]):
            hipotenusa = vetor[1]
            cateto1 = vetor[0]
            cateto2 = vetor[2]
        elif (vetor[2] > vetor[0] and vetor[2] > vetor[1]):
            hipotenusa = vetor[2]
            cateto1 = vetor[0]
            cateto2 = vetor[1]
        print('Hipotenusa: {} Cateto1: {} Cateto2: {}\n'.format(hipotenusa, cateto1, cateto2))
        if (hipotenusa**2 == (cateto1**2 + cateto2**2)):
            return True
        else:
            return False
    if (checkTriangulo(vetorNum)):
        print('O triângulo é retângulo\n')
    else:
        print('O triângulo não é retângulo\n')

# Menu de selecao das funcoes
escolha = 0
while escolha != 4:
    escolha = int(input('Digite qual funcao deseja executar:\n [1] Exercicio 1\n [2] Exercicio 2\n [3] Exercicio 3\n [4] Sair do programa\n'))
    if(escolha == 1):
        exercicio1()
    elif(escolha == 2):
        exercicio2()
    elif(escolha == 3):
        exercicio3()
# Fim do programa
