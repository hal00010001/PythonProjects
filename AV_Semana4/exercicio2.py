#!/usr/bin/python3
#coding: utf-8
valor1 = float(input('Digite um numero: \n'))
if (valor1 < 0):
    print('O valor positivo do numero digitado e {}'.format(abs(valor1)))
elif (valor1 > 10):
    valor2 = float(input('Digite mais um numero: \n'))
    print('A diferenca entre os dois resultados e {}'.format(abs(valor2 - valor1)))
else:
    print('O valor dividido por 5 e {}'.format(valor1 / 5))
