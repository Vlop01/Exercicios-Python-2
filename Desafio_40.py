#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
#média atingida
#-Média abaixo de 5.0: reprovado
#-Média entre 5.0 e 6.9: recuperação
#-Média 7.0 ou superior: aprovado

grade1 = float(input('Informe a primeira nota: '))
grade2 = float(input('Informe a segunda nota: '))

average_grade = (grade1 + grade2) / 2

if average_grade >= 7.0:
    print('Aprovado')
elif average_grade >= 5.0 and average_grade <= 6.9:
    print('Recuperação')
else:
    print('Reprovado')
