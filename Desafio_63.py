#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
#sequência de Fibonacci.
#fui ver o vídeo e achei alguas dicas nos comentários

n = int(input('Informe quantos números deseja ver: '))
fib = 0
cur = 1

while n >= 1:
    n -= 1

    print(fib)
    ant = fib
    fib = fib + cur
    cur = ant
