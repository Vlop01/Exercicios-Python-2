#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
#se o usuário quer ou não continuar. No final mostre:
#A-) Quantas pessoas tem mais de 18 anos
#B-) Quantos homens foram cadastrados
#C-) Quantas mulheres tem menos de 20 anos

count18 = 0
count_men = 0
count_20_women = 0

while True:
    gender = input('Informe o sexo (h/m): ')
    gender = gender.lower()
    if gender == 'h':
        count_men =+ 1

    age = int(input('Informe a idade: '))
    if age > 18:
        count18 =+ 1

    if age < 20 and gender == 'm':
        count_20_women += 1

    Continue = input('Deseja continuar (s/n) ')
    Continue = Continue.lower()

    if Continue == 'n':
        break

print(f'{count18} pessoas tem mais de 18 anos')
print(f'{count_men} são homens')
print(f'{count_20_women} são mulheres com menos de 20 anos')