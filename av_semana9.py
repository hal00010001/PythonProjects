#!/usr/bin/python3
#coding: utf-8

import random

# Exercicio 1
# Crie uma matriz identidade de tamanho NxN, sendo N informado pelo usuário. Crie uma segunda matriz que seja o dobro da primeira.
def exercicio1():
    # Le a variavel dada pelo usuario
    N = int(input('Digite qual sera o tamanho da matriz:\n'))
    matriz = [0]*N
    matrizDobro = [0]*N*2
    # Gera a primeira a matriz
    for i in range(N):
        matriz[i] = [0]*N
    # Transforma em matriz identidade
    for linha in range(N):
        for coluna in range(N):
            if linha == coluna:
                matriz[linha][coluna] = 1
    # Gera a segunda matriz
    for i in range(N*2):
        matrizDobro[i] = [0]*N*2
    # Transforma em matriz identidade
    for linha in range(N*2):
        for coluna in range(N*2):
            if linha == coluna:
                matrizDobro[linha][coluna] = 1
    print('O numero digitado foi {} e a matriz que e o dobro desta sera de tamanho {}\n'.format(N, N*2))
    # Imprime a primeira matriz identidade
    print('Segue abaixo a primeira matriz identidade:\n')
    for j in matriz:
        for k in j:
            print(k, end=' ')
        print('\n')
    print('Segue abaixo a segunda matriz que e o dobro da primeira:\n')
    # Imprime a segunda matriz tabulada
    for j in matrizDobro:
        for k in j:
            print(k, end=' ')
        print('\n')

# Exercicio 2
# Escreva um programa que leia duas matrizes: A de dimensão m x n e B de dimensão n x p e imprima a matriz C de dimensão m x p, que é o produto de A por B.
def exercicio2():
    m = int(input('Digite a dimensao m (tem que ser igual a n e maior ou igual a p):\n'))
    n = int(input('Digite a dimensao n (tem que ser igual a m e maior ou igual a p):\n'))
    p = int(input('Digite a dimensao p:\n'))
    matrizA = [0]*m
    matrizB = [0]*n
    matrizC = []
    # Gerar a matriz A, acresecentando os valores aleatoriamente
    for i in range(m):
        matrizA[i] = [0]*m
    for linha in range(m):
        for coluna in range(n):
            matrizA[linha][coluna] = random.randint(0,10)
    # Gerar a matriz B, acresecentando os valores aleatoriamente
    for i in range(n):
        matrizB[i] = [0]*n
    for linha in range(n):
        for coluna in range(p):
            matrizB[linha][coluna] = random.randint(0,10)
    # Gerar a matriz C, calculando o produto de A e B
    for i in range(m):
        matrizC.append([])
        for j in range(p):
            matrizC[i].append(0)
            for k in range(n):
                matrizC[i][j] += matrizA[i][k] * matrizB[k][j]
    print('Matriz A:\n')
    for j in matrizA:
        for k in j:
            print(k, end=' ')
        print('\n\n')
    print('Matriz B:\n')
    for j in matrizB:
        for k in j:
            print(k, end=' ')
        print('\n')
    print('Matriz C:\n')
    for j in matrizC:
        for k in j:
            print(k, end=' ')
        print('\n')
# Menu de selecao das funcoes
escolha = 0
while escolha != 3:
    escolha = int(input('Digite qual funcao deseja executar:\n [1] Criar matriz que e o dobro da primeira\n [2] Imprimir as matrizes A, B e C\n [3] Sair do programa\n'))
    if(escolha == 1):
        exercicio1()
    elif(escolha == 2):
        exercicio2()
# Fim do programa
