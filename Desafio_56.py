#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final, mostre:
#A media de idade do grupo.
#Qual o nome do homem mais velho
#Quantas mulheres tem menos de 20 anos

average = 0
oldest_man_age = 0
count_women = 0
oldest_man_name = 'none'

for i in range(0, 4):
    name = input('Informe o nome: ')
    age = int(input('Informe a idade: '))
    gender = input('Informe o gênero: ')

    average = average + age / 4

    if (gender == 'm' or gender == 'M') and age > oldest_man_age:
        oldest_man_age = age
        oldest_man_name = name.title()

    if (gender == 'W' or gender == 'w' or gender == 'f' or gender == 'F') and age < 20:
        count_women = count_women + 1

print('O homem mais velho é: {}'.format(oldest_man_name))
print('A média de idade do grupo é: {}'.format(average))
print('{} mulheres tem menos de 20 anos'.format(count_women))