#escreva um programa que leia a velocidade do carro.
#se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#a multa custa R$7 por cada KM acima do limite
print('{:=^30}'.format('Gerador de Multas'))
km = float(input('Informe a KM ultrapassada: '))
if km >= 80:
    print('O condutor ultrapassou a velocidade máxima de 80KM\nA multa aplicada será de R${:.2f}'.format((km - 80) * 7))
else:
    print('O condutor andou no limite da velocidade\nNada a fazer')