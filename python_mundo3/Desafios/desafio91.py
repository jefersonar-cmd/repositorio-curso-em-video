# Crie um programa onde 4 JOGADORES joguem um DADO e teha resultados ALEATORIOS
# Guarde esses resultados em um DICIONARIO
# No final, coloque esse dicionario em ORDEM, sabendo que o VENCEDOR tirou o MAIOR NUMERO no dado.
from random import randint
from time import sleep
dados = {}
for j in range(1, 5):
    dados[j] = randint(1, 6)
    print(f'Jogador {j} jogou {dados[j]}')
    sleep(3)

print('Ordem por vencedores')
lugar = 1
for item in sorted(dados, key=dados.get, reverse=True):
    print(f'Em {lugar}º Luga: Jogador {item} jogou {dados[item]}')
    lugar += 1