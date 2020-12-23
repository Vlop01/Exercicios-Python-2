#Refaça o desafio dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#Equilátero: todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno: todos os lados diferentes

side1 = float(input('Informe o lado 1: '))
side2 = float(input('Informe o lado 2: '))
side3 = float(input('Informe o lado 3: '))

if side1 == side2 and side1 == side3:
    print('Equilátero')
elif side1 == side2 or side1 == side2 or side2 == side3:
    print('Isósceles')
else:
    print("Escaleno")