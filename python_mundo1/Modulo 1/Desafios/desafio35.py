#desenvolva um programa que leia comprimento de tres restas e diga ao usuário se elas
#podem ou nao formar um triangulo
print('-='*20)
print('Analisador de Segmentos')
print('-='*20)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos formam um Triângulo')
else:
    print('Os segmentos não podem formar um Triângulo')