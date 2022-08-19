# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    espaco = len(msg) + 4
    print('-'*espaco)
    print(f'  {msg}')
    print('-'*espaco)

escreva(str(input('Digite algum texto: ')))