#Crie um programa que tenha uma TUPLA
#com VARIOS PALAVRAS (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra,
#quais são as suas VOGAIS
palavras = ('valor', 'adquirir', 'proteger', 'moeda', 'digital', 'contra', 'estatal')
for p in palavras:
    print(f'\nNa plavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')