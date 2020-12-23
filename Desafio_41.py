#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
#sua categoria, de acordo com a idade
#-Até 9 anos: mirim
#-Até 14 anos: infantil
#-Até 19 anos: júnior
#-Acima: master

age = int(input('Informe sua idade: '))

if age <= 9:
    print('Mirim')
elif age <= 14:
    print('Infantil')
elif age <= 19:
    print('Júnior')
else:
    print('Master')