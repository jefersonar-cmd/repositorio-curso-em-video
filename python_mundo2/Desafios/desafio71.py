#crie um programa que
#simule um CAIXA ELETRONICO
#no inicio, pergunte ao usuario qual sera
#o VALOR A SER SACADO (NUMEROS INTEIROS) e o programa
#deve informar quantas CEDULAS de cada valor serao entregues
#OBS.: Considere que o caixa possui cedulas de 50, 20, 10 e 1
print('-='*20)
print('Caixa Eletronico')
print('=-'*20)
valor = int(input('Valor a ser sacado (Sem os Centavos)\nR$'))
cedula = 50
cinquenta = vinte = dez = um = 0
while True:
    while valor > 50:
        if valor < 50:
            break
        else:
            cinquenta += 1
            valor -= 50
            continue
    while valor > 20:
        if valor < 20:
            break
        else:
            vinte += 1
            valor -= 20
            continue
    while valor > 10:
        if valor < 10:
            break
        else:
            dez += 1
            valor -= 10
            continue
    while valor > 1:
        if valor < 1:
            break
        else:
            um += 1
            valor -= 1
            continue
    break
print(f'{cinquenta} notas de Cinquenta')
print(f'{vinte} notas de Vinte')
print(f'{dez} notas de Dez')
print(f'{um} notas de Um')