#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
#No final, mostre:
#A-) Qual é o total gasto na compra
#B-) Quantos produtos custam mais de 1000
#C-) Qual é o nome do produto mais barato

total = 0
plus1000 = 0
i = 0
cheappern = 'NULL'

while True:
    name = input('Informe o produto: ')
    cost = int(input('Informe o preço do produto: '))
    total = total + cost

    if i == 0:
        cheappern = name
        cheapperc = cost

    elif cheapperc > cost:
        cheappern = name
        cheapperc = cost

    if cost > 1000:
        plus1000 =+ 1

    keep = input('Deseja continuar (s/n): ')
    keep = keep.lower()

    if keep == 'n':
        break

print(f'Produto mais barato {cheappern} (R$ {cheapperc}).')
print(f'{plus1000} produtos por mais de R$ 1000,00')
print(f'Total: {total}')