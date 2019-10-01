#!/usr/bin/python3
#coding: utf-8

# Inicio do projeto final: Jogo da Velha
# Recebe os nomes dos dois jogadores
jogador1 = input('Digite o nome do primeiro jogador:\n')
jogador2 = input('Digite o nome do segundo jogador:\n')
tabuleiro = [0]*3
contador = 1

# Gera o tabuleiro
for i in range(3):
    tabuleiro[i] = [0]*3
# Adiciona a sequencia de 1 a 9 para os jogadores poderem selecionar as casas para jogar
for linha in range(3):
    for coluna in range(3):
        tabuleiro[linha][coluna] = contador
        contador += 1

# Funcao para mostrar o tabuleiro aos jogadores
def mostrarTabuleiro(player1, player2):
    print('\n\n\n\n{} e {}, este é o tabuleiro do jogo da velha, onde cada casa a ser escolhida é representada por um número, conforme desenho abaixo:\n\n'.format(player1, player2))
    print('===================\n')
    for j in tabuleiro:
        for k in j:
            print(k, end='  ||  ')
        print('\n')
    print('===================')

# Chamadas das funcoes do codigo
mostrarTabuleiro(jogador1, jogador2)
