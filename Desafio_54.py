#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
#maioridade e quantas já são maiores

cont = 0

for i in range (0, 7):
    age = 2020 - int(input('Informe o ano de nascimento: '))
    if age >= 18:
        cont = cont + 1

print('{} pessoas já atingiram a maioridade'.format(cont))