#!/usr/bin/python3
#coding: utf-8

# Inicio do exercicio 1
# Criar programa que armazene a nota e o nome de 40 estudantes e imprima-os
def exercicio1():
    matriz_turma = []
    for i in range(0, 40):
        matriz_turma_notas = {}
        # Pergunta ao usuario as variaveis nome e nota
        matriz_turma_notas["nome"] = raw_input('Digite o nome do aluno:\n')
        matriz_turma_notas["nota"] = float(input('Digite a nota do aluno:\n'))
        matriz_turma.append(matriz_turma_notas)
    for matriz_turma_notas in matriz_turma:
        print "{nome}: {nota}".format(**matriz_turma_notas)
# Inicio do exercicio 2
# Fazer um programa que leia um vetor de 5 numeros inteiros e mostre-o
def exercicio2():
    vetor = []
    for i in range(0, 5):
        num = int(input('Digite um numero inteiro:\n'))
        vetor.append(num)
    print('O valor do vetor e: {}'.format(vetor))
# Inicio do exercicio 3
# Fazer um programa que leia um vetor de 10 numeros reais e mostre-os na ordem inversa
def exercicio3():
    vetor = []
    for i in range(0, 10):
        num = float(input('Digite um numero real:\n'))
        vetor.append(num)
    print('O vetor em ordem inversa e: {}'.format(vetor[::-1]))
# Inicio do exercicio 4
# Fazer um programa que leia 4 notas e mostre as notas e a media na tela
def exercicio4():
    vetor = []
    for i in range(0, 4):
        num = float(input('Digite uma nota: \n'))
        vetor.append(num)
    print('As notas digitadas sao: {} e a media das notas digitadas e: {}'.format(vetor, sum(vetor)/len(vetor)))
# Inicio do exercicio 5
# Fazer um programa que leia um vetor de 10 caracteres e diga quantas consoantes tem e as imprima
def exercicio5():
    consoantes = []
    vogais = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in range(0, 10):
        caracter = raw_input('Digite um caractere: \n')
        if caracter in vogais:
            count += 1
        else:
            consoantes.append(caracter)
    print('O numero de consoantes digitadas e : {} e elas sao: {}'.format(len(consoantes), consoantes))
# Inicio do exercicio 6
# Fazer um programa que leia 20 numeros inteiros e mostre-os, e tambem mostre os pares e impares
def exercicio6():
    vetorTotal = []
    vetorImpar = []
    vetorPar = []
    for i in range(0, 20):
        num = int(input('Digite um numero inteiro:\n'))
        vetorTotal.append(num)
        if(num % 2 == 0):
            vetorPar.append(num)
        else:
            vetorImpar.append(num)
    print('O vetor par e: {}, o vetor impar e: {} e o vetor com todos os numeros e: {}'.format(vetorPar, vetorImpar, vetorTotal))
# Menu de selecao das funcoes
escolha = 0
while escolha != 7:
    escolha = int(input('Digite qual funcao deseja executar:\n [1] Nomes e notas dos 40 alunos\n [2] 5 numeros inteiros\n [3] 10 numeros reais e mostra na ordem inversa\n [4] 4 notas e a media\n [5] 10 caracteres e imprima as consoantes\n [6] 20 numeros inteiros e separar os pares e impares\n [7] Sair do programa\n'))
    if(escolha == 1):
        exercicio1()
    elif(escolha == 2):
        exercicio2()
    elif(escolha == 3):
        exercicio3()
    elif(escolha == 4):
        exercicio4()
    elif(escolha == 5):
        exercicio5()
    elif(escolha == 6):
        exercicio6()
# Fim do programa
