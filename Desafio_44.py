#Elabore um programa que calculeo valor a ser pago por um produto considerando seu preço normal e condição de pagamento
#À vista dinheiro/cheque: 10% de desconto
#À vista no cartão: 5% de desconto
#Em até 2X no cartão: proço normal
#3X ou mais no cartão: 20% de juros

price = float(input('Informe o preço do produto: '))
option = int (input('''1 - À vista dinheiro/cheque: 10% de desconto
2 - À vista no cartão: 5% de desconto
3 - Em até 2X no cartão: proço normal
4 - 3X ou mais no cartão: 20% de juros
Sua escolha: '''))

if option == 1:
    price = price * 0.9
elif option == 2:
    price = price * 0.95
elif option == 4:
    price = price * 1.20
print('Custo: {}'.format(price))