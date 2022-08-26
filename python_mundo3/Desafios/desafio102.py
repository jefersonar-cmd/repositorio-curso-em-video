# crie um programa que tenha uma FUNÇAO FATORIAL() que receba dois parametros: o primeiro que indique o NUMERO a calcular e o outro chamado SHOW, que será o valor LOGICO (opcional) indicando se será mostrado ou não na tela o processo calculo do fatorial
def fatorial(n=1, show=False):
    f = 1
    dados = []
    for c in range(n, 0, -1):
        dados.append(f)
        f *= c
    if show == True:
        print(f'O fatorial de {n} é ', end='')
        for item in dados:
            print(f'{item}', end=' ')
    else:
        print(f'O fatorial de {n} é igual a {f}')


fatorial(5, show=True)
