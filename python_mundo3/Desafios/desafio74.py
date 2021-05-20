#Crie um programa que vai gerar CINCO NUMEROS ALEATORIOS e
#colocar em uma TUPLA
#Depois disso, mostre a LISTAGEM DE NUMEROS
#gerados e também indique o MENOR e o MAIOR valor que estão na tupla.
from random import randint
tupla = ()
valor = 0
print('Atividade: Tupla registradas aleatóriamente')
for c in range(1, 6):
    valor = randint(0, 100)
    tupla += (valor,)
print('A) Listagem:')
for c in range(0, len(tupla)):
    print(f'{tupla[c]}')
print('B) Maior e menor:')
print(f'O maior número é {max(tupla)}\nE o menor número é {min(tupla)}')