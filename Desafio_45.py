#Faça um programa que faça o computador jogar Jokempô com você

from random import randint

player = input('Pedra, papel tesoura: ')
#1: pedra, 2: papel, 3: tesoura
PC = randint(1, 3)

if PC == 1:
    if player == 'pedra':
        print('Pedra X Pedra: empate')
    elif player == 'papel':
        print('Papel X Pedra: vitória')
    else:
        print('Tesoura X Pedra: derrota')
elif PC == 2:
    if player == 'pedra':
        print('Pedra X Papel: derrota')
    elif player == 'papel':
        print('Papel X Papel: empate')
    else:
        print('Tesoura X Papel: vitória')
elif PC == 3:
    if player == 'pedra':
        print('Pedra X Tesoura: vitória')
    elif player == 'papel':
        print('Papel X Tesoura: derrota')
    else:
        print('Tesoura X Tesoura: empate')