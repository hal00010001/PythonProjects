#!/usr/bin/python3
#coding: utf-8

import random

# Inicio do exercicio 1
# Faça um algoritmo que solicite ao usuário números e os armazene em uma matriz 6x6. Em seguida, crie um vetor que armazene os elementos da diagonal principal da matriz.
def exercicio1():
    vetor = [0]*6
    matriz = [0]*6
    for i in range(6):
        matriz[i] = [0]*6
    for linha in range(6):
        for coluna in range(6):
            matriz[linha][coluna] = input('Digite um valor a ser adicionado:\n')
    print('A matriz e: {}'.format(matriz))
    for linha in range(6):
        for coluna in range(6):
            if linha == coluna:
                vetor[linha] = matriz[linha][coluna]
    print('A matriz impressa de forma tabular e:\n')
    for j in matriz:
        for k in j:
            print(k, end=' ')
        print('\n')
    print('A diagonal principal e: {}'.format(vetor))

# Inicio do exercicio 2
# Tendo uma matriz 10x10 preenchida com valores aleatórios entre 10 e 50, mostre a média dos elementos da diagonal secundária.
def exercicio2():
    matriz = [0]*10
    vetor = [0]*10
    for i in range(10):
        matriz[i] = [0]*10
    for linha in range(10):
        for coluna in range(10):
            matriz[linha][coluna] = random.randint(10,50)
    for linha in range(10):
        for coluna in range(10):
            # O numero 9 corresponde a n+1 que e o numero de colunas da matriz + 1
            if linha + coluna == 9:
                vetor[linha] = matriz[linha][coluna]
    print('A media da diagonal secundaria da matriz e: {}\n'.format(sum(vetor)/len(vetor)))
    for j in matriz:
        for k in j:
            print(k, end=' ')
        print('\n')
    print('A diagonal secundaria e: {}\n'.format(vetor))

# Inicio do exercicio 3
#  Tendo uma matriz 10x10 preenchida com valores aleatórios entre 10 e 50, mostre o maior valor existente desconsiderando os elementos da diagonal principal.
def exercicio3():
    matriz = [0]*10
    vetor = [0]*10
    for i in range(10):
        matriz[i] = [0]*10
    for linha in range(10):
        for coluna in range(10):
            matriz[linha][coluna] = random.randint(10,50)
    for j in matriz:
        for k in j:
            print(k, end=' ')
        print('\n')
    valorMaior = matriz[1][0]
    for linha in range(10):
        for coluna in range(10):
            if(linha != coluna):
                if(matriz[linha][coluna] > valorMaior):
                    valorMaior = matriz[linha][coluna]
    print ('O maior valor da matriz desconsiderando a diagonal principal e {}\n'.format(valorMaior))
# Inicio do exercicio 4
#  Tendo uma matriz 5x5 preenchida com valores aleatórios entre 0 e 99, mostre o segundo maior valor existente.
def exercicio4():
    matriz = [0]*5
    segundoValorMaior = 0
    for i in range(5):
        matriz[i] = [0]*5
    valorMaior = matriz[0][0]
    for linha in range(5):
        for coluna in range(5):
            matriz[linha][coluna] = random.randint(0,99)
    for j in matriz:
        for k in j:
            print(k, end=' ')
        print('\n')
    for linha in range(5):
        for coluna in range(5):
            if(matriz[linha][coluna] > valorMaior):
                valorMaior = matriz[linha][coluna]
    print('O maior valor e: {}\n'.format(valorMaior))
    for linha in range(5):
        for coluna in range(5):
            if(matriz[linha][coluna] > segundoValorMaior and matriz[linha][coluna] != valorMaior):
                segundoValorMaior = matriz[linha][coluna]
    print('O segundo valor maior e: {}\n'.format(segundoValorMaior))

# Menu de selecao das funcoes
escolha = 0
while escolha != 5:
    escolha = int(input('Digite qual funcao deseja executar:\n [1] Diagonal principal de uma matriz\n [2] Media da diagonal secundaria da matriz\n [3] Maior valor existente desconsiderando a diagonal principal\n [4] Segundo maior valor existente\n [5] Sair do programa\n'))
    if(escolha == 1):
        exercicio1()
    elif(escolha == 2):
        exercicio2()
    elif(escolha == 3):
        exercicio3()
    elif(escolha == 4):
        exercicio4()
# Fim do programa
