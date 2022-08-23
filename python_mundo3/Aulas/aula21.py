# Funções e Iteractive Help
def contador(i, f, p):
    """
    -> Teste Interactive Help nas funçoes criadas <-
    => Faz a contagem e mostra na tela <=
    :param i: inicio da contagem
    :param f: final da contagem
    :param p: passos da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM!')

# criado por mim
help(contador)
# nativo python
help(input)

# Parâmetros Opcionais
def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de 3 valores e mostra o resultado na tela <-
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: sem retorno
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(3, 5)
somar(5)
somar()
help(somar)

# Escopo de Variáveis
def teste():
    # variavel local
    global n
    x = 8
    n = x + n
    print(f'Na função o valor de x é {x}')
    print(f'Na função o valor de n é {n}')

# variavel global
n = 2
# print(f'No programa o valor de x é {x}')
print(f'No programa o valor de n é {n}')
teste()

# Retorno de valores

def somar2 (a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar2(3, 5, 2)
r2 = somar2(2, 2)
r3 = somar2(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')

# Na prática

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')