#crie um programa que
#leia o NOME e o PRECO de VARIOS PRODUTOS
#O programa devera perguntar ao USUARIO vai continuar
#no final, mostre:
#A)Qual e o TOTAL GASTO na compra
#B)Quantos produtos custam MAIS de R$1000
#C)Qual e o NOME do produto mais BARATO
from typing import List

print('='*20)
print('''     Lojinha JSA''')
print('='*20)
nomeProduto = []
total = 0
maisCaros = 0
maisBarato = []
cont = ''
contador = 0
valorProduto = []
while True:
    nomeProduto.append(str(input('Informe o nome do produto: ')))
    valor = float(input('Informe o valor: '))
    if valor >= 1000:
        maisCaros += 1
        total += valor
        valorProduto.append(valor)
        cont = str(input('Deseja fechar a conta?\n[S/N]: ')).upper()
        if cont == 'S':
            break
        elif cont == 'N':
            continue
    else:
        total += valor
        valorProduto.append(valor)
        cont = str(input('Deseja fechar a conta?\n[S/N]: ')).upper()
        if cont == 'S':
            break
        elif cont == 'N':
            continue
maisBarato.append(min(valorProduto, key=int))
while True:
    if valorProduto[contador] == maisBarato[0]:
        break
    else:
        contador += 1
        continue
print(f'Total gasto foi de R${total}')
print(f'{maisCaros} produtos passaram dos R$1000')
print(f'O produto mais barato: R${maisBarato[0]}, {nomeProduto[contador]}')