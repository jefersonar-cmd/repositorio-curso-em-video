#faca um programa que mostre na tela
#uma contagem regressiva para o estouro de fogos de artifio
#indo do 10 ATE 0
#Com uma pausa de 1 SEGUNDO entre eles
from time import sleep
print('contagem para os fogos')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('SOLTEM OS FOGOS')