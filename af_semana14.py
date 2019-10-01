#!/usr/bin/python3
#coding: utf-8

import sys

# Inicio do projeto final: Jogo da Velha
# Recebe os nomes dos dois jogadores
jogador1 = input('Digite o nome do primeiro jogador:\n')
jogador2 = input('Digite o nome do segundo jogador:\n')
tabuleiro = [0]*3
jogadas = [0]*3
contador = 1
termino = False
vencedor = ''

# Gera o tabuleiro
for i in range(3):
    tabuleiro[i] = [0]*3
# Adiciona a sequencia de 1 a 9 para os jogadores poderem selecionar as casas para jogar
for linha in range(3):
    for coluna in range(3):
        tabuleiro[linha][coluna] = contador
        contador += 1
# Gerar a matriz de jogadas feitas para comparar
def resetarTabuleiro():
    for i in range(3):
        jogadas[i] = [0]*3

'''def mostrarTabuleiro(player1, player2):
    print('\n\n\n\n{} e {}, este é o tabuleiro do jogo da velha, onde cada casa a ser escolhida é representada por um número, conforme desenho abaixo:\n\n'.format(player1, player2))
    print('===================\n')
    for j in tabuleiro:
        for k in j:
            print(k, end='  ||  ')
        print('\n')
    print('===================')'''

# Funcao para mostrar o tabuleiro aos jogadores
# Unico jeito para ficar mais bonito o tabuleiro foi imprimindo a matriz colocando as posicoes manualmente
# mas deixei o codigo antigo comentado apenas para referencia
def mostrarTabuleiro(player1, player2):
    print('\n\n\n\n{} e {}, este é o tabuleiro do jogo da velha, onde cada casa a ser escolhida é representada por um número, conforme desenho abaixo:\n\n'.format(player1, player2))
    print('===================================\n')
    print('||    {}    ||    {}    ||    {}    ||'.format(tabuleiro[0][0], tabuleiro[0][1], tabuleiro[0][2]))
    print('===================================\n')
    print('||    {}    ||    {}    ||    {}    ||'.format(tabuleiro[1][0], tabuleiro[1][1], tabuleiro[1][2]))
    print('===================================\n')
    print('||    {}    ||    {}    ||    {}    ||'.format(tabuleiro[2][0], tabuleiro[2][1], tabuleiro[2][2]))
    print('===================================\n')

# Funcao que grava a posicao com o numero escolhido, representando cada jogador
def tValor(matriz, i, j):
    if(matriz[i][j] == 1):
        return 1
    elif(matriz[i][j] == 2):
        return 2
    else:
        return 'Livre'

# Imprimir o tabuleiro no decorrer do jogo, com as casas marcadas com o jogador1, jogador2 ou livre
def mostrarTabuleiroDuranteJogo():
    print('===============================================\n')
    print('||    {}    ||    {}    ||    {}    ||'.format(tValor(jogadas,0,0), tValor(jogadas,0,1), tValor(jogadas,0,2)))
    print('===============================================\n')
    print('||    {}    ||    {}    ||    {}    ||'.format(tValor(jogadas,1,0), tValor(jogadas,1,1), tValor(jogadas,1,2)))
    print('===============================================\n')
    print('||    {}    ||    {}    ||    {}    ||'.format(tValor(jogadas,2,0), tValor(jogadas,2,1), tValor(jogadas,2,2)))
    print('===============================================\n')

# Funcao para checar se o jogo terminou
def checarTermino(player1, player2):
    global vencedor
    if(jogadas[0][0] == 1 and jogadas[0][1] == 1 and jogadas[0][2] == 1):
        vencedor = player1
        return True
    elif(jogadas[0][0] == 1 and jogadas[1][0] == 1 and jogadas[2][0] == 1):
        vencedor = player1
        return True
    elif(jogadas[1][0] == 1 and jogadas[1][1] == 1 and jogadas[1][2] == 1):
        vencedor = player1
        return True
    elif(jogadas[2][0] == 1 and jogadas[2][1] == 1 and jogadas[2][2] == 1):
        vencedor = player1
        return True
    elif(jogadas[0][1] == 1 and jogadas[1][1] == 1 and jogadas[2][1] == 1):
        vencedor = player1
        return True
    elif(jogadas[0][2] == 1 and jogadas[1][2] == 1 and jogadas[2][2] == 1):
        vencedor = player1
        return True
    elif(jogadas[0][0] == 1 and jogadas[1][1] == 1 and jogadas[2][2] == 1):
        vencedor = player1
        return True
    elif(jogadas[0][2] == 1 and jogadas[1][1] == 1 and jogadas[2][0] == 1):
        vencedor = player1
        return True
    # Inicio de verificacao do jogador2
    elif(jogadas[0][0] == 2 and jogadas[0][1] == 2 and jogadas[0][2] == 2):
        vencedor = player2
        return True
    elif(jogadas[0][0] == 2 and jogadas[1][0] == 2 and jogadas[2][0] == 2):
        vencedor = player2
        return True
    elif(jogadas[1][0] == 2 and jogadas[1][1] == 2 and jogadas[1][2] == 2):
        vencedor = player2
        return True
    elif(jogadas[2][0] == 2 and jogadas[2][1] == 2 and jogadas[2][2] == 2):
        vencedor = player2
        return True
    elif(jogadas[0][1] == 2 and jogadas[1][1] == 2 and jogadas[2][1] == 2):
        vencedor = player2
        return True
    elif(jogadas[0][2] == 2 and jogadas[1][2] == 2 and jogadas[2][2] == 2):
        vencedor = player2
        return True
    elif(jogadas[0][0] == 2 and jogadas[1][1] == 2 and jogadas[2][2] == 2):
        vencedor = player2
        return True
    elif(jogadas[0][2] == 2 and jogadas[1][1] == 2 and jogadas[2][0] == 2):
        vencedor = player2
        return True
    else:
        verificarEmpate()
        return False

# Funcao para verificar se deu empate e pergunta se deseja jogar novamente
def verificarEmpate():
    if (jogadas[0][0] != 0 and jogadas[0][1] != 0 and jogadas[0][2] != 0 and jogadas[1][0] != 0 and jogadas[1][1] != 0 and jogadas[1][2] != 0 and jogadas[2][0] != 0 and jogadas[2][1] != 0 and jogadas[2][2] != 0):
        resposta = input('O jogo acabou, e terminou em empate, deseja jogar novamente? [S/N]')
        if (resposta == 'S' or resposta == 's'):
            iniciarNovaPartida()
        else :
            print('Obrigado, jogadores')
            sys.exit()

# Funcao que ira validar a jogada conforme a escolha do jogador
# Se a jogada for valida, a matriz jogadas mudara o valor do campo para True
def validarJogada(player, num, player1, player2):
    for linha in range(3):
        for coluna in range(3):
            if (tabuleiro[linha][coluna] == num and jogadas[linha][coluna] == 0):
                jogadas[linha][coluna] = player;
                return True
            #elif(jogadas[linha][coluna] != 0):
            #    jogar(player1, player2)
            #elif(jogadas[linha][coluna] == 1 or jogadas[linha][coluna] == 2):
            #    return False

# Funcao que vai pedir para os jogadores fazerem suas e validar as mesmas
def jogar(player1, player2):
    global vencedor
    while checarTermino(player1, player2) == False:
        mostrarTabuleiroDuranteJogo()
        num = int(input(print('\n\n{} pode selecionar o número que corresponde à casa desejada:\n'.format(player1))))
        if (num >= 1 or num <= 9):
            validarJogada(1, num, player1, player2)
        if (checarTermino(player1, player2) == False):
            mostrarTabuleiroDuranteJogo()
            num = int(input(print('\n\n{} pode selecionar o número que corresponde à casa desejada:\n'.format(player2))))
            if (num >= 1 or num <= 9):
                validarJogada(2, num, player1, player2)
    # Pergunta se os jogadores querem jogar novamente ou terminar o programa
    resposta = input('O jogo acabou, o(a) vencedor(a) foi {}, deseja jogar novamente? [S/N]'.format(vencedor))
    if (resposta == 'S' or resposta == 's'):
        iniciarNovaPartida()
    else :
        print('Obrigado, jogador(a) {}'.format(vencedor))
        sys.exit()

# Chamadas das funcoes do codigo
def iniciarNovaPartida():
    resetarTabuleiro()
    mostrarTabuleiro(jogador1, jogador2)
    jogar(jogador1, jogador2)

# Ponto de partida do programa
iniciarNovaPartida()
