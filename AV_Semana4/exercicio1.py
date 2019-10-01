#!/usr/bin/python3
#coding: utf-8
import math

numero = float(input("Digite um numero entre 1 e 9, exceto 5:\n"))
if (numero == 1 or numero == 2 or numero == 3):
    print('O resultado do valor elevado ao quadrado e: {}'.format(numero ** 2))
elif (numero == 4 or numero == 9):
    print('O resultado da raiz quadrada do valor e: {}'.format(math.sqrt(numero)))
elif (numero == 6 or numero == 7 or numero == 8):
    print('O resultado do valor dividido por nove e: {}'.format(numero / 9))
else:
    print('O numero que voce digitou nao esta entre 1 e 9 ou e o numero 5')
