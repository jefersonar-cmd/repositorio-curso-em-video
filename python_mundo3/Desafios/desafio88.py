# Faça um programa que ajude um jogador da MEGA SENA a criar PALPITES. O programa vai perguntar
# QUANTOS JOGOS serão gerados e vai sortear 6 NUMEROS ENTRE 1 E 60 para cada jogo, cadastrando tudo em uma LISTA COMPOSTA.
from random import randint
print('Sorteio da Mega Senha')
lista = []
composta = []
numero = 0
qtd = int(input('Informe a Quantidade de Jogos para Mega Sena: '))
for q in range(0, qtd):
    for n in range(0, 6):

