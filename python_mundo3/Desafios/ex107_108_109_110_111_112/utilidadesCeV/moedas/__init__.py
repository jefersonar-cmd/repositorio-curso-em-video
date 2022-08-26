def aumentar(n=1, p=10, formatar=False):
    p = p / 100
    v = n * p
    v = n + v
    if formatar:
        return moeda(v)
    else:
        return v


def reducao(n=1, p=3, formatar=False):
    p = p / 100
    v = n * p
    v = n - v
    if formatar:
        return moeda(v)
    else:
        return v


def dobro(n, formatar=False):
    n = n * 2
    if formatar:
        return moeda(n)
    else:
        return n


def metade(n, formatar=False):
    n = n / 2
    if formatar:
        return moeda(n)
    else:
        return n


def moeda(parametro):
    return f'{parametro:.2f}'


def resumo(valor, aumento=80, diminuir=30):
    """
    -> Resumo da moeda
    :param valor: recebe preço
    :param aumento: recebe porcentagem de aumento no preço desejado
    :param diminuir: recebe porcentagem de redução no preço desejado
    :return: retorna o dados formatados na tela
    """
    return f"{'Preço analizado':<20} R${moeda(valor)}\n" \
           f"{'Dobra do preço':<20} R${dobro(valor, formatar=True)}\n" \
           f"{'Metade do Preço':<20} R${metade(valor, formatar=True)}\n" \
           f"{aumento}% {'de aumento':<16} R${aumentar(valor, aumento, formatar=True)}\n" \
           f"{diminuir}% {'de redução':<16} R${reducao(valor, diminuir, formatar=True)}"