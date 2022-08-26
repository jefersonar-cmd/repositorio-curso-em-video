import moeda

nota = float(input('Informe um valor: '))
print(f'Valor aumentado em 10%: {moeda.aumentar(nota)}')
print(f'Valor diminuido em 3%: {moeda.reducao(nota)}')
print(f'Valor dobrado: {moeda.dobro(nota)}')
print(f'Valor pela metade: {moeda.metade(nota)}')