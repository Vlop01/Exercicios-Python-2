#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo a
#tabela abaixo:
#Abaixo de 18.5: abaixo do peso
#Entre 18.5 e 25: peso ideal
#25 até 30: sobrepeso
#30 até 40: obesidade
#Acima de 40: obesidade mórbida

height = float(input('Informe sua altura: '))
weight = float(input('Informe seu peso: '))

IMC = weight / (height**2)

if IMC < 18.5:
    print('Abaixo do peso')
elif IMC < 25:
    print('Peso ideal')
elif IMC < 30:
    print('Sobrepeso')
elif IMC < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')