# faça uma aplicação que leia
# as duas notas do aluno,
# calcule e mostre a sua média

nome = str(input('Informe o nome do aluno: '))

n1 = float(input('Informe a primeira nota do aluno {}: '.format(nome)))
n2 = float(input('Informe a primeira nota do aluno {}: '.format(nome)))

media = (n1+n2)/2

if media >= 7:
    print('Parabenize o aluno {} que obteve a média {}'.format(nome, media))
else:
    print('Informe o aluno {} para se esforçar mais. A média dele foi de {}'.format(nome, media))