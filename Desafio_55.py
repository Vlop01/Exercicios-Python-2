#Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e menor peso lidos

for i in range(0,5):
    weight = input('Informe o peso: ')
    if i == 0:
        lighter = weight
        heaviest = weight
    else:
        if weight < lighter:
            lighter = weight
        if weight > heaviest:
            heaviest = weight
print('O maior peso foi: {}\nO menor peso foi: {}'.format(heaviest, lighter))