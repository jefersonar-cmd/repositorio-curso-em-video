#Escreva um programa que
#leia um NUEMRO n INTEIRO qualquer
#e mostre na tela os N primeiros elementos
#de uma SEQUENCIA DE FIBONACCI
#EX 0 1 1 2 3 5 8
print('Fibonacci')
limite = int(input('Escolha um limite'))
n1 = 0
n2 = 1
while limite != 0:
    print(n1, n2, end=' ')
    n1 = n1 + n2
    n2 = n1 + n2
    limite -= 1
print('FIM')