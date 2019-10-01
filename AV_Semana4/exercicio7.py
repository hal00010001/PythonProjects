#!/usr/bin/python3
#coding: utf-8
numero1 = float(input('Digite o primeiro numero:\n'))
numero2 = float(input('Digite o segundo numero:\n'))
numero3 = float(input('Digite o terceiro numero:\n'))
if(numero1 > numero2 and numero1 > numero3):
    print('O maior numero digitado e {}'.format(numero1))
    if(numero2 > numero3):
        print('O menor numero digitado e {}'.format(numero3))
    else:
        print('O menor numero digitado e {}'.format(numero2))
elif(numero2 > numero1 and numero2 > numero3):
    print('O maior numero digitado e {}'.format(numero2))
    if(numero1 > numero3):
        print('O menor numero digitado e {}'.format(numero3))
    else:
        print('O menor numero digitado e {}'.format(numero1))
elif(numero3 > numero1 and numero3 > numero2):
    print('O maior numero digitado e {}'.format(numero3))
    if(numero1 > numero2):
        print('O menor numero digitado e {}'.format(numero2))
    else:
        print('O menor numero digitado e {}'.format(numero1))
