#!/usr/bin/python3
#coding: utf-8
numero1 = int(input('Digite o primeiro numero inteiro:\n'))
numero2 = int(input('Digite o segundo numero inteiro:\n'))
if(numero1 > numero2):
    print('O primeiro valor e maior')
elif(numero2 > numero1):
    print('O segundo valor e maior')
else:
    print('Nao existe valor maior, os dois sao iguais')
