#faca um programa que
#jogue PAR OU IMPAR com o computador
#o jogo so sera interrompido quando o jogador PERDER,
#mostrando o total de vitorias consecutivas que ele conquistou
#no final do jogo
from random import randint
soma = 0
cont = 0
print('Jogar PAR ou IMPAR')
while True:
    user = int(input('Informe um valor: '))
    comp = randint(0, 100)
    pi = str(input('[P/I]: ')).upper()
    total = user + comp
    if pi == 'P':
        if total % 2 == 0:
            print('Parabens')
            cont += 1
        else:
            print('Perdeu')
            break
    elif pi == 'I':
        if total % 2 == 0:
            print('Perdeu')
            break
        else:
            print('Parabens')
            cont += 1
print(f'Voce Perdeu!\nSuas Vitorias Consecutivas: {cont}')