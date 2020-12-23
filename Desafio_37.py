#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher aqual sera a base de conversão
#1 para binário
#2 para octal
#3 para hexadecimal

num = int(input('Informe o número: '))
option = int(input('Informe qual a opção:\n1 para binário\n2 para octal\n3 para hexadecimal\nSua escolha: '))

if option == 1:
    print('O valor em binário é: {}'.format(bin(num)))
elif option == 2:
    print('O valor em octal é: {}'.format(oct(num)))
elif option == 3:
    print('O valor em hexadecimal é: {}'.format(hex(num)))
else:
    print('Informe uma opção válida')