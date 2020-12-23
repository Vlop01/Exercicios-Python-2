#Faça um programa que leia um número qualquer e mostre o seu fatorial

num = int(input('Informe um número: '))
fat = 1

while num > 1:
    fat = fat * num
    num -= 1

print('Fatorial: {}'.format(fat))