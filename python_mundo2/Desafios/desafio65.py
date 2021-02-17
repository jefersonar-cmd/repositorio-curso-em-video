#crie um programa que
#leia VARIOS NUMEROS inteiros pelo teclado
#No final da execucao, mostre a MEDIA ENTRE ELES
#e qual foi o MAIOR e o MENOR valor lido.
#O programa deve perguntar ao usuario se ele QUER ou NAO
#CONTINUAR a digitar os valores
print('Numeros aleatorios')
cont = 0
total = 0
array = []
user = 'Z'
while user != 'N':
    numero = int(input('Informe um numero inteiro: '))
    cont += 1
    total += numero
    array.append(numero)
    print('Deseja Continuar?\n[S/N]')
    user = str(input('Escolha: ')).upper()
print('O maior numero informado foi {}\nO menor numero informado foi {}\nA media entre todos os numeros foi de {}'.format(max(array, key=int), min(array, key=int), total/cont))