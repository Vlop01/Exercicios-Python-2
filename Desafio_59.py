#Crie um programa que leia dois valores e mostre um menu na tela:
#1 somar
#2 multiplicar
#3 maior
#4 novos números
#5 sair do programa

num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))
option = 0

while option != 5:
    option = int(input('''Deseja:
    1 - Somar
    2 - Multiplicar
    3 - Ver qual o maior
    4 - Escolher novos números
    5 - Sair do programa
    Sua opção: '''))

    if option == 1:
        sum = num1 + num2
        print('Soma: {}'.format(sum))
    elif option == 2:
        mult = num1 * num2
        print('Multiplicação: {}'.format(mult))
    elif option == 3:
        if num1 > num2:
            greatest = num1
        elif num2 > num1:
            greatest = num2
        else:
            greatest = 'none'
        print('Maior número: {}'.format(greatest))
    elif option == 4:
        num1 = int(input('Informe o novo número: '))
        num2 = int(input('Informe o outro novo número: '))