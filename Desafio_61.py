#Refaça o desafio 51, lendo o primeiro termo de uma PA e mostrando os 10 primeiros termos da progressão usando a
#estrutura while

first = int(input('Informe o primeiro termo da PA: '))
rate = int(input('Informe a razão da PA: '))
i = 1

print(first)

while i < 10:
    first = first + rate
    print(first)
    i += 1