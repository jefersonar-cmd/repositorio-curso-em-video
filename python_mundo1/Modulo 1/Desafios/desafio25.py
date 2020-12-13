#crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome
nome = str(input('Digite seu nome Completo: '))
print('Verificando seu nome comeca com SILVA')
print('...')
nome = nome.upper()
resultado = 'SILVA' in nome
resultado = str(resultado)
if resultado == 'True':
    print('O nome contem SILVA')
else:
    print('Não contem SILVA')