#Escrev aum programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
#da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não vai pode exceder 30% do salário ou netão o empréstimo
#será negado
value = float(input('Informe o valor da casa: '))
salary = float(input('Informe o seu salário: '))
time = float(input('Informe em quantos anos você deseja pagar: '))

installment = value / (time * 12)

if installment > (salary * 0.3):
    print('Empréstimo não foi aprovado')
else:
    print('Emprestimo aprovado')

