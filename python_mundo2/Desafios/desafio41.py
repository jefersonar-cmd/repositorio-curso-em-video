#a confederacao nacional de natacao precisa de uma programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
#ate 9 anos: mirim
#ate 14 anos: infantil
#ate 19 anos: junior
#ate 20 anos: senior
#acima: master
from datetime import datetime
anoAtual = datetime.now()
anoAtual = anoAtual.year
print('-='*20)
print('Classificação de Natação')
print('=-'*20)
nascimento = int(input('Informe o ano de nascimento: '))
idade = anoAtual - nascimento
if idade <= 9:
    print('Mirim')
elif idade > 9 and idade <= 14:
    print('Infantil')
elif idade > 14 and idade <= 19:
    print('Junior')
elif idade > 19 and idade <= 20:
    print('Senior')
else:
    print('Master')