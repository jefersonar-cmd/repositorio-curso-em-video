# crie um programa que tenha uma FUNCAO chamado FICHA(), que receba dois PARAMETROS OPCIONAIS: o NOME de um jogador e quantos GOLS ele marcou
# O programa deverá ser capaz de mostrar a FICHA DO JOGADOR, mesmo que algum dado não tenha sido informado corretamente
def ficha(nome='<DESCONHECIDO>', gols=0):
    print(f'O jogador {nome} fez {gols} gols')


nome = str(input('Digite o nome do jogador: '))
golacos = str(input('Digite a qtd de gols: '))
if golacos.isnumeric():
    g = int(golacos)
else:
    g = 0
if nome.strip() == '':
    ficha(gols=g)
else:
    ficha(nome, golacos)