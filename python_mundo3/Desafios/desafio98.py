#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep
def title():
    titulo = 'Contador'
    tam = len(titulo) + 4
    print('-'*tam)
    print(f'  {titulo}')
    print('-'*tam)


def contador(inicio, fim, passos):
    texto = f'Contando do {inicio} até {fim} indo de {passos}'
    tam = len(texto) + 4
    print('-=' * tam)
    print(f'  {texto}')
    if passos < 0:
        passos *= -1
    if passos == 0:
        passos = 1
    if inicio < fim:
        while inicio <= fim:
            print(f'{inicio}', end=' ', flush=True)
            sleep(0.5)
            inicio += passos
    else:
        while inicio >= fim:
            print(f'{inicio}', end=' ', flush=True)
            sleep(0.5)
            inicio -= passos
    print('FIM!')
    print('-='*tam)

title()
contador(1, 10, 1)
contador(10, 0, 2)
title()
i = int(input('Digite o número inicial do contador: '))
f = int(input('Digite o número final do contador: '))
p = int(input('Digite o número de passos do contador: '))
contador(i, f, p)