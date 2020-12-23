#Faça um programa que leia um número inteiro e diga se ele é ou não primo

num = int(input('Informe um número: '))
cont = 1

for i in range (2, num):
    if(num % i == 0):
        cont = 0

if cont:
    print('{} é primo'.format(num))
else:
    print('{} não é primo'.format(num))