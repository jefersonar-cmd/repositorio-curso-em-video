# Fazer uma aplicação que leia
# um número inteiro e mostre na tela
# o seu sucessor e seu antecessor

n1 = int(input('Informe um valor inteiro: '))
sus = 0
ant = 0

print('O valor informado foi: {}. E seu antecessor é: {}. E seu sucessor é: {}'.format(n1, n1 - 1, n1 + 1))