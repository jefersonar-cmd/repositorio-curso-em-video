# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(list):
    a = list[0] * list[1]
    print(f'A área total do terreno de {list[0]}x{list[1]} é de {a}m².')


dimensoes = list()
dimensoes.append(float(input('Largura (m): ')))
dimensoes.append(float(input('Comprimento (m): ')))
area(dimensoes)