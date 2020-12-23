#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça
#a digitação novamente até ter uma valor correto

for i in range (0, 10):
    gender = input('Informe o sexo da pessoa[F/M]: ')

    while gender != 'F' and gender != 'M':
        gender = input('Infome corretamente, por favor:')

    if gender == 'M':
        print('Homem')
    else:
        print('Mulher')