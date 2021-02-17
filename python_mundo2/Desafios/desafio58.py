#melhore o jogo do DESAFIO 28
#onde o computador vai "pensar"
#em um NUMERO ENTRE 0 e 10
#so que agora o jogador vai tentar adivinhar ate acertar,
#mostrando no final quantos palpites foram necessários para vencer
from random import randint
from time import sleep
pc = randint(0, 10)
cont = 0
print('A Pensar..')
sleep(3)
user = int(input('Adivinhe o numero que o computador pensou.\nEscolha de 0 a 10\n'))
print('Jogo da adivinhacao')
while user != pc:
    user = int(input('Errou! Tente novamente.\nEscolha de 0 a 10\n'))
    cont += 1
print('Parabens! Voce ganhou. O pc jogou {}. E tu tentou {} vezes'.format(pc, cont))
