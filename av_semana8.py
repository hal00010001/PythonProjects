#!/usr/bin/python3
#coding: utf-8

# Inicio do exercicio 1
# Fazer um programa que peca as quatro notas de 10 alunos, armazenar a media e imprimir os alunos com media 7
def exercicio1():
    nomes = []
    notas = []
    media = 7
    alunos = 10
    for i in range(alunos):
        nomes.append(input('Digite o nome do aluno:\n'))
        nota_1 = float(input('Digite a primeira nota\n'))
        nota_2 = float(input('Digite a segunda nota\n'))
        nota_3 = float(input('Digite a terceira nota\n'))
        nota_4 = float(input('Digite a quarta nota\n'))
        notas.append((nota_1 + nota_2 + nota_3 + nota_4)/4)
    for i in range(alunos):
        if notas[i] >= media:
            print('Parabens {}'.format(nomes[i]))
# Inicio do exercicio 2
# Fazer um programa que leia um vetor de 5 numeros inteiros e mostre a soma, a multiplicacao e os numeros
def exercicio2():
    vetor = []
    multi = 1
    for i in range(0, 5):
        num = int(input('Digite um numero:\n'))
        vetor.append(num)
    for x in vetor:
        multi = multi * x
    print('A soma dos numeros digitados e {}, a multiplicacao e {} e os numeros sao {}'.format(sum(vetor), multi, vetor))
# Inicio do exercicio 3
# Fazer um programa que leia um indeterminado numero de valores ate -1 e faca o seguinte:
# Quantidade de valores lidos
# Valores na ordem que foram digitados, um ao lado do outro
# Valores na ordem inversa, um abaixo do outro
# Soma entre eles
# Media entre eles
# Quantidade acima da media
# Valores abaixo de 7
# Encerrar com uma mensagem
def exercicio3():
    num = 0
    vetor = []
    i = 1
    while num != -1:
        num = float(input('Digite um numero:\n'))
        if(num != -1):
            vetor.append(num)
    print('a. A quantidade de valores lidos e: {}\n'.format(len(vetor)))
    print('b. Valores digitados: {}\n'.format(vetor))
    print('c. Valores na ordem inversa: \n')
    while i <= len(vetor):
        print ('{}\n'.format(vetor[len(vetor)-i]))
        i = i + 1
    print('d. A soma dos valores e: {}\n'.format(sum(vetor)))
    print('e. A media dos valores e: {}\n'.format(sum(vetor)/len(vetor)))
    print('f. Os valores acima da media sao:\n')
    for i in range(len(vetor)):
        if vetor[i] >= (sum(vetor)/len(vetor)):
            print('{} '.format(vetor[i]))
    print('g. Os valores abaixo de 7 sao:\n')
    for i in range(len(vetor)):
        if vetor[i] < 7:
            print('{} '.format(vetor[i]))
    print('h. Fim do exercicio 3')
# Inicio do exercicio 4
# Fazer um programa que receba a temperatura media de cada mes do ano e armazene-os.
# Depois calcular a media anual e mostre todas acima da media e em que mes ocorreram por extenso
def exercicio4():
    temp = []
    tempMedia = 0
    mes = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    for i in range(len(mes)):
        temp.append(float(input('Digite a temperatura do mes de {}:\n'.format(mes[i]))))
    tempMedia = (sum(temp)/len(mes))
    print('A media anual das temperaturas e de: {}\n'.format(tempMedia))
    print('Os meses que tiveram temperaturas acima da media foram:\n')
    for i in range(len(mes)):
        if temp[i] > tempMedia:
            print('{} - {}\n'.format(i +1, mes[i]))
# Menu de selecao das funcoes
escolha = 0
while escolha != 5:
    escolha = int(input('Digite qual funcao deseja executar:\n [1] Medias de 10 alunos\n [2] 5 numeros inteiros, soma e multiplicacao\n [3] Numero indeterminado de valores\n [4] Temperatura media anual\n [5] Sair do programa\n'))
    if(escolha == 1):
        exercicio1()
    elif(escolha == 2):
        exercicio2()
    elif(escolha == 3):
        exercicio3()
    elif(escolha == 4):
        exercicio4()
# Fim do programa
