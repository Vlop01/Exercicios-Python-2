#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário
#O programa será interrompido quando o número solicitado for negativo
#Obs: esse faz parte da aula de interromper repetições, portanto faz sentido usar break

while True:
    num = int(input('Informe um número: '))

    if num < 0:
        print('Fim do programa, obrigado')
        break

    for i in range(0, 11):
        print(f'{num} X {i} = {num * i}')