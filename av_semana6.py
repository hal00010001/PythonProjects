#!/usr/bin/python3
#coding: utf-8

# Inicio do exercicio 1
# Calcular o fatorial de um numero utilizando for
numFatFor = int(input('Digite um numero inteiro para obter o resultado fatorial utilizando o \"for\"\n'))
countFor = numFatFor
fatFor = 1
for i in range(1, numFatFor + 1):
    fatFor = fatFor * i
print('O fatorial de {} e {}'.format(numFatFor, fatFor))
# Inicio do exercicio 2
# Calcular o fatorial de um numero utilizando while
numFatWhile = int(input('Digite um numero inteiro para obter o resultado fatorial utilizando o \"while\"\n'))
countWhile = numFatWhile
fatWhile = 1
while countWhile > 0:
    fatWhile = fatWhile * countWhile
    countWhile -=1
print('O fatorial de {} e {}'.format(numFatWhile, fatWhile))

# Inicio do exercicio 3
# Mostrar a tabuada do numero digitado
numTab = int(input('Digite um numero inteiro para ver a sua tabuada\n'))
print('A tabuada do numero {} e:\n'.format(numTab))
print('{}'.format(numTab * 1))
print('{}'.format(numTab * 2))
print('{}'.format(numTab * 3))
print('{}'.format(numTab * 4))
print('{}'.format(numTab * 5))
print('{}'.format(numTab * 6))
print('{}'.format(numTab * 7))
print('{}'.format(numTab * 8))
print('{}'.format(numTab * 9))
print('{}'.format(numTab * 10))

# Inicio do exercicio 4
# Calcular a soma entre todos os numeros multiplos de 3 no intervalo de 1 a 500
soma3 = 0
for i in range(1, 500):
    if(i % 3 == 0):
        soma3 = soma3 + i
print('O resultado da soma dos multiplos de 3 entre 1 e 500 e {}'.format(soma3))

# Inicio do exercicio 5
# Calcular a soma somente dos numeros pares entre os 6 numeros que foram digitados
soma6 = 0
for i in range (1, 7):
    num6 = int(input('Digite um numero: \n'))
    if (num6 % 2 == 0):
        soma6 = soma6 + num6
print('O resultado da soma dos numeros pares dos seis numeros digitados e {}'.format(soma6))

# Inicio do exercicio 6
# Calcular a progressao aritmetica utilizando os numeros digitados
numPrimTermo = int(input('Digite o primeiro termo da progressao aritmetica\n'))
razaoPA = int(input('Digite a razao da progressao aritmetica\n'))
numDecTermo = numPrimTermo + (10 -1) * razaoPA
for i in range(numPrimTermo, numDecTermo, razaoPA):
    print('- {} - '.format(i))
print('Fim')
# Inicio do exercicio 7
# Verificar se o numero digitado e primo ou nao
numPrimo = int(input('Digite um numero para descobrir se e primo: \n'))
numDiv = 0
for i in range(2, numPrimo + 1):
    if (numPrimo % i == 0):
        numDiv += 1
if(numDiv > 1):
    print('O numero nao e primo')
else:
    print('O numero e primo')

# Inicio do exercicio 8
# Obter os dois valores digitados
opCalc = 0
while opCalc != 5:
    numCalc1 = int(input('Digite o primeiro numero a ser calculado\n'))
    numCalc2 = int(input('Digite o segundo numero a ser calculado\n'))
    opCalc = int(input('Escolha a operacao desejada: \n[1] Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos numeros\n[5]Sair do programa\n'))
    if(opCalc == 1):
        print('O resultado da soma dos valores e {}'.format(numCalc1 + numCalc2))
    elif(opCalc == 2):
        print('O resultado da multiplicacao dos valores e {}'.format(numCalc1 * numCalc2))
    elif(opCalc == 3):
        if(numCalc1 > numCalc2):
            print('O maior numero e o {}'.format(numCalc1))
        elif(numCalc2 > numCalc1):
            print('O maior numero e o {}'.format(numCalc2))
        else:
            print('Os numeros sao iguais')
    elif(opCalc == 5):
        print('Fim do programa')

# Multipla escolha para decidir qual operacao matematica fazer
