import moeda

nota = float(input('Informe um valor: '))
print(f'Valor aumentado em 30%: R${moeda.aumentar(nota, 0.3, formatar=True)}')
print(f'Valor diminuido em 5%: R${moeda.reducao(nota, 0.05, formatar=True)}')
print(f'Valor dobrado: R${moeda.dobro(nota, formatar=True)}')
print(f'Valor pela metade: R${moeda.metade(nota, formatar=True)}')