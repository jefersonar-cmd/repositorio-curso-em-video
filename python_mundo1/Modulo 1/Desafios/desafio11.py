# faça uma aplicação que leia a
# largura e a altura de uma parede
# em metros, calcule a sua área e a
# quantidade de tinta necessária para
# pintá-la, sabendo que cada litro de
# tinta, pinta uma área de 2m²

print('{:=^30}'.format('Quanto de tinta Usarei?'))
n1 = float(input('Informe a largura da parede (em metros): '))
n2 = float(input('Informe a altura da parede (em metros): '))
print('Sua parede tem {} metros largura e {} metros de altura.'.format(n1, n2))
print('Sua parede tem {}m²'.format(n1 * n2))
print('Você precisará de {} litros de tinta'.format((n1 * n2) / 2))
