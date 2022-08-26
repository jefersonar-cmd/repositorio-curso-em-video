# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(*num):
    print('-='*20)
    print('Analizando os valores passados...')
    print(num)
    for valor in num:
        print(valor, end=' ')
    if len(num) == 0:
        print(f'Foram informados {len(num)} ao todo.')
        print(f'O maior valor informado foi {len(num)}')
    else:
        print(f'\nForam informados {len(num)} ao todo.')
        print(f'O maior valor informado foi {max(num)}')
    print('-='*20)


maior(2,5,7,9)
maior(5,6,2,1,4)
maior(1,2)
maior()