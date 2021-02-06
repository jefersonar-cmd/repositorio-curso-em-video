#elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preco normal e condicao de pagamento:
#a vista dinheiro/cheque: 10% de desconto
#a vista no cartao: 5% de desconto
#em ate 2x no cartao: preco normal
#3x ou mais no cartao: 20% de juros
from time import sleep
print('-='*20)
print('Condições de Venda')
print('=-'*20)
valorProduto = float(input('Informe o valor do produto:\nR$'))
print('Escolha uma opção:\n1-A vista Dinheiro/Cheque\n2-A vista Cartão\n3-2x no cartão\n4-3x ou mais no cartão')
escolha = int(input('Escolha: '))
if escolha == 1:
    print('Dinheiro/Cheque')
    print('Calculando..')
    sleep(3)
    desconto = valorProduto * 0.1
    valorProduto -= desconto
    print('Descontado 10% (R${:.2f}), valor a pagar R${:.2f}'.format(desconto,valorProduto))
elif escolha == 2:
    print('Cartão A Vista')
    print('Calculando..')
    sleep(3)
    desconto = valorProduto * 0.05
    valorProduto -= desconto
    print('Descontado 5% (R${:.2f}), valor a pagar R${:.2f}'.format( desconto ,valorProduto))
elif escolha == 3:
    print('2x no Cartão')
    print('Calculando..')
    sleep(3)
    parcela = valorProduto / 2
    print('Parcelamento de até 2x de R${:.2f}. Total de R${:.2f}'.format(parcela,valorProduto))
elif escolha == 4:
    print('3x ou Mais no Cartão')
    print('Máxima de 24x com Juros')
    print('Calculando..')
    sleep(3)
    contador = 3
    valorJuros = valorProduto * 0.2
    valorProduto += valorJuros
    while contador <= 24:
        parcela = valorProduto / contador
        print('Parcelas {} de R${:.2f}. Total R${:.2f}'.format(contador, parcela, parcela*contador))
        if contador == 24:
            print('Agradecemos pela preferência')
            break
        contador += 1
else:
    print('Opção inválida.')
print('Agradecemos por Usar nosso Programa')