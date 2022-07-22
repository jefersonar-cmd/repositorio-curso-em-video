# Aprimore o DESAFIO 93 para que ele funcione com VARIOS JOGADORES
# incluindo um sistema de visualização de DETALHES DO APROVEITAMENTO de CADA JOGADOR
from string import whitespace
from time import sleep
jogador = {}
aproveitamento = []
qtd = 0
while True:
    qtd += 1
    jogador['id'] = qtd
    jogador['nome'] = str(input('Informe Jogador: '))
    jogador['partidas'] = int(input('Informe quantidades de partidas: '))
    gols = []
    gtotal = gol = 0
    for g in range(0, jogador['partidas']):
        gol = int(input(f'Gols na {g+1}ª Partida: '))
        gols.append(gol)
        gtotal += gol
    jogador['gols'] = gols
    jogador['gtotal'] = gtotal
    aproveitamento.append(jogador.copy())
    jogador.clear()
    if str(input('Deseja continuar? [S/N]: ')).upper() == 'N':
        break
    else:
        continue

print('Verificando dados...')
sleep(3)
print(f'{"id":<4}{"nome":>8}{"Gols":>8}{"GTotal":>8}')
for a in range(0, len(aproveitamento)):

