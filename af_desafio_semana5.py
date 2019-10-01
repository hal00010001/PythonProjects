#!/usr/bin/python3
#coding: utf-8

# Inicio do programa para converter decimal para binario
num_decimal = int(input('Digite um numero inteiro para ser convertido para binario\n'))
num_binario = ''
# Funcao para conversao
def convertDecBin(num_decimal):
    num_binario = ''
    while (True):
        num_binario = num_binario + str(num_decimal % 2)
        num_decimal = num_decimal // 2
        if num_decimal == 0:
            break
    num_binario = num_binario[::-1]
    num_binario = int(num_binario)
    return num_binario
print('O numero digitado convertido para binario e: {}'.format(convertDecBin(num_decimal)))
