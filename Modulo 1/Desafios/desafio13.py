# faça um algorítmo que leia
# o salário de um funcionário
# e mostre seu novo salário,
# com 15% de aumento

print('{:=^50}'.format('Aumento de Salário'))
nome = str(input('Informe o nome do funcionário: '))
n1 = float(input('Informe o salário atual do mesmo: R$'))

print('O funcionário {} teve aumento de R${} para R${}'.format(nome, n1, n1 + (n1 * 0.15)))
