#Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele
#disser que ver mostrar mais 0 termos

first = int(input('Informe o primeiro termo da PA: '))
rate = int(input('Informe a razão da PA: '))
num = int(input('Deseja ver quantos termos? '))

while num != 0:
    i = 0
    while i < num:
        first = first + rate
        print(first)
        i += 1

    num = int(input('Deseja ver mais quantos números? '))