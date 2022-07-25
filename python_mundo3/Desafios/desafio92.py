# crie um programa que leia NOME, ANO DE NASCIMENTO CTPS e cadastre-os (com IDADE) em um DICIONARIO
# se por acaso a CTPS for diferente de ZERO, o dicionario recebera também o ANO DE CONTRATACAO
# e o SALARIO. calcule e acrescente, alem da IDADE, com quantos anos a pessoa vai se APONSENTAR.
from datetime import datetime
aposentadoria = {}
aposentadoria['nome'] = str(input('Digite o nome: '))
aposentadoria['nascimento'] = int(input('Digite o ano de nascimento: '))
aposentadoria['ctps'] = int(input('Digite o numero da CTPS (0 para quem não tem): '))
if aposentadoria['ctps'] == 0:
    for i, v in aposentadoria.items():
        print(f'{i}: {v}')
else:
    idade = datetime.now().year
    aposentadoria['idade'] = idade - aposentadoria['nascimento']
    aposentadoria['aposentadoria'] = aposentadoria['idade'] + 35

for i, v in aposentadoria.items():
    print(f'{i}: {v}')