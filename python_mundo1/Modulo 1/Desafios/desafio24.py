#crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome 'SANTO'
nome = str(input('Digite o nome de uma cidade ou estado: '))
print('Verificando se o nome da cidade ou estado comeca com SANTOS')
print('...')
nome = nome.upper()
resultado = 'SANTOS' in nome
resultado = str(resultado)
if resultado == 'True':
    print('O nome contem SANTOS')
else:
    print('Não contem SANTO')