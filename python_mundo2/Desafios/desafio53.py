#crie um programa que
#leia uma FRASE qualquer
#e diga se ela é um PALINDROMO
#desconsiderando os espacos
frase = str(input('Digite uma frase abaixo\n'))
frase = frase.replace(' ', '')
frase = frase.lower()
palindromo = frase[::-1]
if palindromo == frase:
    print('É um palindromo')
else:
    print('Nao é um palindromo')