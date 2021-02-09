#faca um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#se ele ainda vai se alistar ao servico militar
#se é a hora de se alistar
#se já passou do tempo do alistamento
#o programa tambem devera mostrar o tempo que falta ou que passou do prazo
import datetime, time
ano = datetime.datetime.now()
ano = ano.year
print('-='*20)
print('Alistamento')
print('=-'*20)
nascimento = int(input('Informe o seu ano de nascimento: '))
print('Verificando..')
time.sleep(3)
idade = ano - nascimento
if idade < 18:
    print('Ainda falta muito para seu ano de alistamento')
    alista = 18 - idade
    print('Falta {} anos para seu alistamento'.format(alista))
elif idade == 18:
    print('Está na hora de se alistar')
elif idade > 18:
    print('Já passou da hora de se alistar')
    alista = idade - 18
    print('Passou {} anos do seu alistamento.'.format(alista))