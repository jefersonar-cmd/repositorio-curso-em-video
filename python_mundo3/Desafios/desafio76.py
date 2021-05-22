#Crie uma TUPLA unica com NOMES DE PRODUTOS e seus respectivos PREÇOS, na sequencia.
#No final, mostre uma listagem de preços,
#organizando os dados em forma TABULAR
lista = ('Lápis', 1.30, 'Caneta', 3.00, 'Caderno', 35.90)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end='')
    else:
        print(f' R${lista[c]:.2f}')