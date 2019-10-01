#!/usr/bin/python3
#coding: utf-8
valor1 = float(input('Digite um numero: \n'))
if (valor1 == 1 or valor1 == 2):
    print('O resultado do valor ao cubo e {}'.format(valor1 ** 3))
elif (valor1 % 3 == 0):
    fatorial = 1
    while (valor1 > 0):
        fatorial = fatorial * valor1
        valor1 -= 1
    print('O fatorial do valor digitado e {}'.format(fatorial))
elif (valor1 == 4 or valor1 == 5 or valor1 == 7 or valor1 == 8):
    print('O resultado do valor dividido por 9 e {}'.format(valor1 / 9))
else:
    print('Valor invalido')
