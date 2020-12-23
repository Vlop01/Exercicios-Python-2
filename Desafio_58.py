#Melhore o jogo do desafio 28 onde o compurador vai pensar em um número entre 0 e 10. Só que agora o jogador vai
#tentar adivinhar até acertar, mostrando no final quantos palpites foram nocessários para vencer

from random import randint

count = 1
Pc = randint(0, 10)
player = int(input('Qual número o computador pensou? '))

if player == Pc:
    print('Parabéns, você acertou de primeira!!!')

else:
    while player != Pc:
        print('A não, você errou, tente novamente')
        player = int(input('Qual é o número? '))
        count += 1

    print('Você acertou em {} tentativas'.format(count))