#Faça um programa que calcule a soma entre todos os numeros ímpares qie são múltiplos de 3 e que se encontram no
#intervalo de 1 até 100

s = 0

for i in range (1, 501):
    if i % 2 != 0 and i % 3 == 0:
        s =+ i
print(s)