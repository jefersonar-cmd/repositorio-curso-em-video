# escreva um programa que faca o computador pensar em um numero inteiro entre 0 e 5
# e peca para o usuário tentar descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu
import random

aleatorio = random.randint(0, 5)
print('{:=^50}'.format('Utilize números de 0 a 5'))
usr = int(input('Tente adivinhar o numero sorteado: '))
if usr == aleatorio:
    print('Meus Parabéns, voce acertou!!')
else:
    print('Infelizmente voce errou!\nTente mais na próxima vez')
