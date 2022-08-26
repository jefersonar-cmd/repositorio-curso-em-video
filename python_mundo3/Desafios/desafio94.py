# crie um programa que leia NOME, SEXO e IDADE de VARIAS PESSOAS, guardando os dados de cada pessoa
# em um DICIONARIO e todos os dicionarios em uma LISTA.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) Uma lista de todas as MULHERES
# C) Uma lista com todas as pessoas com IDADE acima da MEDIA.
from time import sleep
pessoas = {}
lista = []
media = fem = 0
while True:
    pessoas['nome'] = str(input('Informe o Nome: '))
    pessoas['sex'] = str(input('Informe o Sexo [M/F]: ')).upper()
    pessoas['idade'] = int(input('Informe a idade: '))
    media += pessoas['idade']
    lista.append(pessoas.copy())
    pessoas.clear()
    if str(input('Deseja continuar? [S/N]\n')).upper() == 'N':
        break
    else:
        continue
print('Verificando dados...')
sleep(2)
print('-='*30)
print(f'Pessoas Cadastradas: {len(lista)}')
for m in range(0, len(lista)):
    if lista[m]['sex'] == 'F':
        fem += 1
print(f'Total de Mulheres: {fem}')
media = int(media / len(lista))
print('Pessoas Acima da Média de Idade:')
print(f'Media de idade: {media}')
for m in range(0, len(lista)):
    if lista[m]['idade'] > media:
        print(f'Nome: {lista[m]["nome"]}, Sexo: {lista[m]["sex"]}, Idade: {lista[m]["idade"]}')