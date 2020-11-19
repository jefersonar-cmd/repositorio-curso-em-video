# faça um algorítmo que leia o
# preço de um produto e mostre seu
# novo preço, com 5% de desconto

print('{:=^50}'.format('Desconto do Produto'))
nome = str(input('Informe o nome do produto: '))
n1 = float(input('Informe o valor do Produto R$'))

print('O produto {} com desconto aplicado sai por R${:.2}'.format(nome, n1-(n1*0.05)))