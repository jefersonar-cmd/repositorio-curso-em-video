# faça uma aplicação que leia
# quanto dinheiro uma pessoa
# tem na carteira a mostra quantos
# dólares ela pode comprar
# cotação atual 18/11 = 5,36

print('{:=^30}'.format('Carteira && Dolar'))
carteira = float(input('Informe o quanto tem em carteira R$'))
print('Sua carteira tem R${} \nO dolar está custando R${}'.format(carteira, 5.36))
print('Você poderá comprar U${:.2f}'.format(carteira/5.36))