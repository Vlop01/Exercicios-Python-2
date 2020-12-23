#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint

victory = 0

while True:
    computer = randint(0, 1)
    player = int(input('Informe o número: '))
    option = input('Par ou ímpar? ')
    option = option.lower()

    result = player + computer

    if option == 'par':
        if result % 2 == 0:
            victory += 1
            print('Vitória')

        else:
            print('Derrota')
            print(f'Total de vitórias: {victory}')
            break;

    else:
        if result % 2 != 0:
            victory += 1
            print('Vitória')

        else:
            print('Derrota')
            print(f'Total de vitórias: {victory}')
            break;