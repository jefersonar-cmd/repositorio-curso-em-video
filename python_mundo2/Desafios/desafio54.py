#crie um programa que
#leia o ANO DE NASCIMENTO de SETE PESSOAS
#no final, mostre quantas pessoas nao atingiram
#a maioridade e quantas ja sao maiores
from datetime import datetime
atual = datetime.now().year
idade = 0
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Informe o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = atual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('{} pessoas sao maiores e {} sao menores de idade'.format(maior, menor))