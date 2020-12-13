#Criar um programa que leia o nome completo de uma pessoa e mostre
# O nome com todas as letras maiusculas
# O nome com todas minusculas
# Contar quantas letras ao todo (sem considerar os espacos)
# Quantas letras tem o primeiro nome

frase = str('Ana Maria de Souza').strip()
print('Nome com letras minusculas: {}'.format(frase.lower()))
print('Nome com letras maiusculas: {}'.format(frase.upper()))
print('Quantos caracteres utilizados: {}'.format(len(frase) - frase.count(' ')))
nome = frase.split()
print('Quantidade de letras no primeiro nome: {}'.format(len(nome[0])))