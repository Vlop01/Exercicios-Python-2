#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
#dessa progressão

first = int(input('Informe o primeiro termo da PA: '))
rate = int(input('Informe a razão da PA: '))

print(first)
for i in range(0, 9):
    first = first + rate
    print(first)