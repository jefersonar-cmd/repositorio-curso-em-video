# faça um programa que tenha uma FUNCAO NOTAS() que pode receber várias notas de alunos e vai retornar um DICIONARIO com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média de turma
# - A situação (opcional)
# Adicione também os DOCSTRINGS da função
def notas(*nota, situ=False):
    """
    -> tirar media e situação notas da sala
    :param nota: recebe as notas
    :return: retorna as qtd de nota, maior nota, menor nota, media e situação (opcional)
    """
    qtd = len(nota)
    maior = max(nota)
    menor = min(nota)
    media = sum(nota)/len(nota)
    if situ:
        if media >= 7.0:
            return f'Notas: {qtd}; Maior: {maior}; Menor: {menor}; Média: {media}; Situação: Ótima!'
        elif media >= 5 and media < 7:
            return f'Notas: {qtd}; Maior: {maior}; Menor: {menor}; Média: {media}; Situação: Razoável!'
        else:
            return f'Notas: {qtd}; Maior: {maior}; Menor: {menor}; Média: {media}; Situação: Ruim!'
    else:
        return f'Notas: {qtd}; Maior: {maior}; Menor: {menor}; Média: {media}'


print(notas(7,6,3,9,8, situ=True))
help(notas)