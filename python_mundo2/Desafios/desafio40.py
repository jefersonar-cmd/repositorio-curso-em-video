#crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atingida
#media baixo de 5.0: Reprovado
#media entre 5.0 e 6.9: Recuperação
#media 7.0 ou superior: Aprovado
print('-='*20)
print('Media do Aluno')
print('=-'*20)
nt1 = float(input('Informe a nota 1: '))
nt2 = float(input('Informe a nota 2: '))
media = (nt1 + nt2) / 2
if media >= 7:
    print('Aluno aprovado')
elif media > 5 and media <= 6.9:
    print('Aluno de Recuperação')
elif media <= 5:
    print('Aluno Reprovado')