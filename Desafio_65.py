#Crie um programa que leia vários números inteiros pelo teclado. No final de cada execução, mostre a média entre
#todos os valores e qual foi o maior e menor valor lido. O programa deve perguntar ao usuário se ele quer ou não
#continuar a digitar valores

continuar = 'sim'
count = 0
sum = 0

while continuar == 'sim' or continuar == 'Sim' or continuar == 'SIM' or continuar =='S' or continuar == 's':
    num = int(input('Informe um número: '))
    continuar = input('Deseja continuar[S/N]? ')

    if count == 0:
        greatest = num
        smallest = num
    else:
        if num > greatest:
            greatest = num
        if num < smallest:
            smallest = num

    count += 1
    sum = sum + num

if count > 0:
    average = sum / count
else:
    average = 'None'

print('A média entre os números é: {}'.format(average))
print('O maior número é: {}'.format(greatest))
print('O menor número é: {}'.format((smallest)))