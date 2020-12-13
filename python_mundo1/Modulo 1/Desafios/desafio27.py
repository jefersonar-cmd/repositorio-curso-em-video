# faca um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
# Ex.: Ana Maria de Souza
# Primeiro.: Ana
# Ultimo.: Souza
nome = input('Digite seu nome completo: ').strip()
name = nome.split()
print('Seu primeiro nome é: {}'.format(name[0]))
print('Seu ultimo nome é: {}'.format(name[len(name) - 1]))
