# Crie um programa que leia um número REAL qualquer pelo teclado e mostre a sua porção inteira
# Ex.: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

from math import floor
num = float(input('Digite um número flutuante: '))
print('O numero {} tem a parte inteira {}'.format(num, floor(num)))