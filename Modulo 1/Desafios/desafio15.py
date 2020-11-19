# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Por quantos dias o carro foi alugado? '))
km_rod = float(input('E quantos KM rodados? '))

res_dias = dias * 60
res_km = km_rod * 0.15
total = res_dias + res_km
print('Você alugou por {} dias, rodou {}KM. Tudo lhe custou R${:2}'.format(dias, km_rod, total))
