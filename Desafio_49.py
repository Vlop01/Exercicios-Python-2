#Refaça o desafio 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando laço for

num = int(input('Informe um número: '))

for i in range(0, 11):
    print('{} * {} = {}'.format(num, i, num * i))