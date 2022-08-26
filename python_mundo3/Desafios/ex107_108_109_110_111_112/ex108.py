import moeda

nota = float(input('Informe um valor: '))
print(f'Valor aumentado em 10%: R${moeda.moeda(moeda.aumentar(nota))}')
print(f'Valor diminuido em 3%: R${moeda.moeda(moeda.diminuir(nota))}')
print(f'Valor dobrado: R${moeda.moeda(moeda.dobro(nota))}')
print(f'Valor pela metade: R${moeda.moeda(moeda.metade(nota))}')