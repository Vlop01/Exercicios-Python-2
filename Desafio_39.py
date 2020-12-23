#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#-Se ele ainda vai se alistar ao serviço militar
#-Se é a hora de se alistar
#-Se já passou do tempo de alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

born = int(input('Qual o ano de seu nascimento: '))

if 2020 - born < 18:
    remaining = (2020 - born - 18) * (-1)
    print('Ainda não é hora de você se alistar, faltam {} ano(s)'.format(remaining))
elif 2020 - born > 18:
    late = 2020 - born - 18
    print('Já se passaram {} ano(s) desde que você deveria ter se alistado'.format(late))
else:
    print('Você deve se alistar esse ano')