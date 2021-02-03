#faca um programa que leia um ano qualquer e mostre se ele é BISSEXTO
print('{:=^30}'.format('Verificador de Ano Bissexto'))
ano = int(input('Que ano quer analisar? Caso queira o ano atual: digite 0\n'))
from datetime import date
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 and ano % 400 == 0:
    print('{}. É um ano Bissexto'.format(ano))
else:
    print('{}. Não é ano Bissexto'.format(ano))