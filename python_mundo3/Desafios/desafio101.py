# Crie um programa que tenha um FUNÇÃO chamada voto() que vai receber um PARAMETRO o ANO DE NASCIMENTO de uma pessoa, RETORNANDO um valor LITERAL indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.
def voto(ano):
    """
    -> verificar se o cidadão é obrigado ou não a votar... <-
    :param ano: recebe o ano de nascimento
    :return: retorna NEGADO se idade menor que 16 anos, OBRIGATORIO se entre 18 à 69 anos ou OPCIONAL caso entre 16, 17 ou acima dos 70 anos
    """
    from datetime import datetime
    atual = datetime.now().year
    idade = atual - ano
    if idade >= 16 and idade <= 17 or idade >= 70:
        return f'O cidadão tem {idade} e é OPCIONAL VOTAR'
    elif idade >= 18 and idade < 70:
        return f'O cidadão tem {idade} e é OBRIGATÓRIO VOTAR'
    elif idade < 16:
        return f'O cidadão tem {idade} e é NEGADO VOTAR'


nasc = voto(int(input('Digite o ano de nascimento: ')))
print(nasc)