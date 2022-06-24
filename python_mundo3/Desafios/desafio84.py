# Faça um programa que leia NOME E PESO de VÁRIAS PESSOAS, guardando tudo em uma LISTA. No final, mostre:
#a) QUANTAS pessoas foram cadastradas
#b) Uma lista com as pessoas mais PESADAS
#c) Uma listagem com as pessoas mais LEVES
from time import sleep
lista = []
pessoa = []
while True:
    pessoa.append(str(input('Digite o nome: ')))
    pessoa.append(float(input('Agora o peso: ')))
    lista.append(pessoa[:])
    pessoa.clear()
    continuar = str(input('Deseja continuar? [s/n]'))
    if continuar.upper() == 'S':
        continue
    else:
        break

print('Verificando dados inseridos...')
sleep(5)
print(f'Foram cadastradas {len(lista)} pessoas.')
pesos = []
maiores = []
menores = []
for p in lista:
    if p[1] <= 70.0:
        menores.append(p)
    elif p[1] > 70.0 or p[1] <= 80.0:
        continue
    elif p[1] > 80.0:
        maiores.append(p)

print('Pessoas com maiores pesos:')
for m, ps in maiores:
    print(f'{m} pesa {ps}KG')

print('Com menores peso')
for n, ps in menores:
    print(f'{n} pesa {ps}KG')
print('Obrigado por utilizar o aplicativo')
