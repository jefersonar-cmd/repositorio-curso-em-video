#Escreva um programa que leia Dois Numeros inteiros e compare-os, mostrando na tela uma mensagem
# o Primeiro é maior
# o Segundo é maior
# Nao existe valor maior, os dois sao iguais
from time import sleep
print('-='*20)
print('Comparador de Números')
print('=-'*20)
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
print('Pensando..')
sleep(4)
if n1 > n2:
    print('O primeiro número é maior')
elif n1 < n2:
    print('O segundo número é maior')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais')