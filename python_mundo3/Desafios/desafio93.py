# crie um programa que gerencie o aproveitamento de um JOGADOR DE FUTEBOL.
# O programa vai ler o NOME, QUANTAS PARTIDAS ele jogou.
# Depois vai ler a QUANTIDADE DE GOLS feitos em CADA PARTIDA.
# No final, tudo isso será guardado em um DICIONARIO, incluindo o TOTAL DE GOLS feitos durante o campeonato.
from time import sleep
aproveitamento = {}
aproveitamento['nome'] = str(input('Qual nome do Jogador: '))
aproveitamento['partidas'] = int(input('Qual a quantidade de Partidas Jogadas: '))
gols = []
for g in range(0, aproveitamento['partidas']):
    gols.append(int(input(f'Gols da partida {g+1}: ')))
aproveitamento['gols'] = gols
aproveitamento['gtotal'] = 0
for g in range(0, len(gols)):
    aproveitamento['gtotal'] += gols[g]
print(aproveitamento)
print('Calculando e Formatando...')
sleep(3)
print('-='*30)
print(f'Jogador: {aproveitamento["nome"]}.\nJogou {aproveitamento["partidas"]} partidas.')
for g in range(0, len(gols)):
    print(f'Gols na {g+1}ª Partida: {gols[g]}')
print(f'Com total de {aproveitamento["gtotal"]} Gols no campeonato.')
print('-='*30)
sleep(1)
print('Obrigado Por Utilizar O Programa de Analise de Aproveitamento!')