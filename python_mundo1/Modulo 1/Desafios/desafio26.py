#faca um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letra 'A'
#em que posicao ela aparece a primeira vez
#em que posicao ela aparece a ultima vez
frase = input('Digite uma frase: ').lower().strip()
print('Verificando quantas letras -a- contem na sua frase')
print('...')
print('Temos {} letras -a- dentro da frase'.format(frase.count('a')))
print('A letra -a- aparece na posicao: {}'.format(frase.find('a')))
print('A letra -a- e a ultima vez aparece na posicao: {}'.format(frase.rfind('a')))