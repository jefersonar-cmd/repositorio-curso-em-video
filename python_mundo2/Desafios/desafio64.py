#crie um programa que
#leia VARIOS NUMEROS INTEIROS pelo teclado.
#O programa so vai parar quando o usuario digitar
#o valor 999, que eh a CONDICAO DE PARADA
#No final, mostre
#QUANTOS NUMEROS foram digitados e qual foi a SOMA entre
#eles (desnconsiderando o FLAG)
print('Tomando Numeros')
tudo = []
contagem = 0
user = 0
total = 0
while user != 999:
    user = int(input('Informe um numero qualquer\n'))
    tudo.append(user)
    total += user
    contagem += 1
    if user != 999:
        continue
    else:
        user = 999
        print('Parando programa')
print('O maior eh {} e o menor numero {} e a soma dos mesmos eh de {}'.format(max(tudo, key=int), min(tudo, key=int), total))