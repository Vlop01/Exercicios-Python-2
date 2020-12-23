#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

phrase_org = input('Diga uma frase: ')
list = phrase_org.split()
phrase = ''.join(list)
phrase = phrase.lower()
cont = 1

for i in range(0, len(phrase)):
    if phrase[i] != phrase[len(phrase) -1 - i]:
        cont = 0

if cont:
    print('{} é palíndromo'.format(phrase_org))
else:
    print('{} não é palíndromo'.format(phrase_org))