# Aprimore o DESAFIO 93 para que ele funcione com VARIOS JOGADORES
# incluindo um sistema de visualização de DETALHES DO APROVEITAMENTO de CADA JOGADOR
from string import whitespace
from time import sleep
jogador = {}
jogadores = {}
ids = 1
while True:
    jogador['nome'] = str(input('Informe o Nome do Jogador: '))
    jogador['partidas'] = int(input('Informe Quantidade de Partidas: '))
    partidas = jogador['partidas']
    gols = []
    gtotal = 0
    for g in range(0, partidas):
        gols.append(int(input(f'Informe QTD de Gols da {g+1}ª Partida: ')))
    jogador['gols'] = gols
    for g in range(0, partidas):
        gtotal += gols[g]
    jogador['gtotal'] = gtotal
    jogadores[ids] = jogador.copy()
    ids += 1
    jogador.clear()
    if str(input('Deseja adicionar mais?[S/N] ')).upper() == 'N':
        break
    else:
        continue

print('Calculando...')
sleep(2)
print(f"{'ID':<4}{'Nome':<8}{'Partidas':<12}{'Gols':<8}")
for i, j in jogadores.items():
    print(f"{i:<4}{j['nome']:<8}{j['partidas']:<12}{j['gtotal']:<8}")
while True:
    idper = int(input(f'Deseja ver mais detalhes de qual jogador?\nDigite o ID ou 999 para finalizar o programa\nR: '))
    if idper == 999:
        break
    else:
        print(f"ID: {idper}\nNome: {jogadores[idper]['nome']}\nPartidas: {jogadores[idper]['partidas']}")
        gols = jogadores[idper]['gols']
        for g in range(0, len(gols)):
            print(f"    Gols da {g+1}ª Partida: {gols[g]}")
        print(f"Total de Gols no Campeonato: {jogadores[idper]['gtotal']}")
        continue

print('Finalizando programa.\nObrigado por Utilizar! ^-^/')