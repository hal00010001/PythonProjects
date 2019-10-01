#!/usr/bin/python3
#coding: utf-8
km = float(input('Qual a distancia da viagem desejada em km?\n'))
if (km <= 200):
    print('O preco da passagem e R$ {}'.format(km * 0.50))
else:
    print('O preco da passagem e R$ {}'.format(km * 0.45))
