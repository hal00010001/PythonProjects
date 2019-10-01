#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import random
#Created on Sun Sep  9 19:18:49 2018

# Inicio do exercicio 1

# Condicao se o valor digitado estiver ok, imprime o resultado, senao pede outro valor que seja valido
num = input("Por favor digite um numero entre 1 e 10\n")
while (num < 1 or num > 10):
    num = input("Por favor digite um numero entre 1 e 10\n")
print('O numero {} e valido e esta entre os numeros 1 e 10'.format(num))

# Inicio do exercicio 2

# Checando se o numero gerado aleatoriamente e igual ao numeo digitado pelo ususario no exercicio anterior
rdm = random.randint(1,10)
while (num is not rdm):
    rdm = random.randint(1,10)
    if (num is not rdm):
        print('O numero {} ainda nao e igual ao numero digitado pelo usuario'.format(rdm))
print('O numero {} gerado aleatoriamente e igual ao digitado!'.format(rdm))

# Inicio do exercicio 3
x = input('Digite um valor entre 1 e 10\n')

# Inicio do loop for para gerar os numeros aleatoriamente x vezes
for i in range(x):
    rd = random.randint(1,10)
    print('Impressao numero {}'.format(i))
    print('O numero gerado aleatoriamente e {}'.format(rd))

# Inicio do exercicio 4
numero1 = input('Digite o primeiro numero\n')
numero2 = input('Digite o segundo numero\n')
soma = 0

# Inicio do loop for para imprimir todos os numeros pares entre os dois numeros
for i in range (numero1,numero2):
    if (i % 2 == 0):
        soma = soma + i
print('A soma dos pares entre os dois numeros digitados e : {}'.format(soma))
