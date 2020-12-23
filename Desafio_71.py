#Crie um programa que simule o funcionamento de um caixa eletrônco. No início, pergunte ao usuário qual será o valor a
#ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#Obs: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
#Inf: vou considerar que possui cédulas infinitas de cada tipo

saque = int(input('Informe quanto deseja sacar: '))
count50 = 0
count20 = 0
count10 = 0
count1 = 0

while saque > 0:

    if saque >= 50:
        saque = saque - 50
        count50 += 1
    elif saque >= 20:
        saque = saque - 20
        count20 += 1
    elif saque >= 10:
        saque = saque - 10
        count10 += 1
    elif saque >= 1:
        saque = saque - 1
        count1 += 1

print('Foram usadas {} notas de R$50, {} notas de R$20, {} notas de R$10 e {} notas de R$1'.format(count50, count20, count10, count1 ))