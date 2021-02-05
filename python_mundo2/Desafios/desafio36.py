#Escreva um programa para aprovar o emprestimo bancario para compra de uma casa.
#O programa devera perguntar o Valor da Casa, o Salario do comprador e em Quantos Anos ele vai pagar.
#Calcule o valor da prestacao mensal, sabendo que ela não pode exceder 30% do salario ou entao o emprestimo sera negado.
from time import sleep
print('-='*20)
print('Bem-Vindo ao Programa de Crédito Pessoal em Imoveis')
print('=-'*20)
print('Vamos Começar')
valorCasa = float(input('Informe o valor da casa:\nR$'))
salarioComprador = float(input('Informe o salário:\nR$'))
anosPagando = int(input('Em quantos anos deseja pagar?\n'))
mesesPagando = anosPagando * 12
trintaPorcento = salarioComprador * 0.3
valorMensal = valorCasa / mesesPagando
print('Calculando..')
sleep(3)
taxa = valorMensal * 0.032
valorMensal += taxa
print('Verificando Condições..')
sleep(3)
if valorMensal <= trintaPorcento:
    print('Meus parabéns!\nVocê é elegível para o Programa.')
    print('Você irá pagar R${:.2f} durante {} meses.'.format(valorMensal, mesesPagando))
    print('Total a pagar R${:.2f}'.format(valorMensal*mesesPagando))
    print('Entraremos em contato em breve')
elif valorMensal > trintaPorcento:
    print('Infelizmente, você não é elegível ao Programa.\nO valor da prestação excede os 30% do seu salário...')
    print('Tente mais tarde')
print('Muito obrigado por utilizar o programa.\nO dev Agradece ^^')