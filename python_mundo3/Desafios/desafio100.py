# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint


def sorte():
    numeros = []
    qtd = 0
    while qtd < 5:
        numero = randint(1, 100)
        erro = 'n'
        if len(numeros) == 0:
            numeros.append(numero)
            qtd += 1
        try:
            numeros.index(numero)
        except:
            erro = 's'
        if erro != 'n':
            numeros.append(numero)
            qtd += 1
    print(f'Números sorteados \n{sorted(numeros)}')
    somaPar(numeros)


def somaPar(numero):
    somaTudo = par = 0
    for item in numero:
        if item % 2 == 0:
            somaTudo += item
            par += 1
    print(f'A soma de todos os {par} números PARES Somados: {somaTudo}')

sorte()