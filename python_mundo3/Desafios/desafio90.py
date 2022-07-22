# Faça um programa que leia NOME E MEDIA de uma aluno,
# guardando também a SITUACAO em um DICIONARIO.
# No final, mostre o conteúdo da estrutura na tela.
aluno = {}
aluno['nome'] = str(input('Digite o Nome do Aluno: '))
aluno['media'] = float(input('Qual foi a media do aluno: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

print(f'Aluno: {aluno["nome"]}\nMedia: {aluno["media"]}\nSituação: {aluno["situacao"]}')