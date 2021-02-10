#crie um programa que faca o computador jogar jokenpo com voce
from random import randint
numeros = [1, 2, 3]
print('-='*20)
print('Jokenpo com o Computador')
print('-='*20)
print('Escolha um:\n1) Pedra\n2) Tesoura\n3) Papel')
jogador = int(input('R: '))
computador = randint(1, 3)
if computador == 1:
    print('Computador jogou Pedra')
    if jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Computador jogou venceu')
    elif jogador == 3:
        print('Você ganhou')
elif computador == 2:
    print('Computador jogou Tesoura')
    if jogador == 1:
        print('Jogador Ganhou')
    elif jogador == 2:
        print('Empate')
    elif jogador == 3:
        print('Computador Ganhou')
elif computador == 3:
    print('Computador jogou Papel')
    if jogador == 1:
        print('Computador ganhou')
    elif jogador == 2:
        print('Jogador ganhou')
    elif jogador == 3:
        print('Empate')

