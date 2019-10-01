#!/usr/bin/python3
#coding: utf-8

# Recebe a frase digitada pelo usuario
frase = str(input('Digite a frase que deseja: \n'))

# Inicio da funcao que retorna a ultima palavra de uma frase
def printUltimaPalavra(sentenca):
    resultado = sentenca.split()
    return resultado[len(resultado)-1]
# Imprime a ultima palavra da frase
print('A ultima palavra que voce digitou em sua frase foi: {}'.format(printUltimaPalavra(frase)))
# Fim do programa
