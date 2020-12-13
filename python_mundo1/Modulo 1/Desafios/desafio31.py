#Desenvolva um programa que pergunte a distancia de uma viagem em KM.
#Calcule o preco da passagem, cobrando R$0.50 por KM para viagens de até 200KM
#e R$0.45 para viagens mais longas
print('{:=^30}'.format('Verificador de Passagem'))
distancia = float(input('Informe a distancia (em KM) para calcularmos sua passagem: '))
if distancia <= 200:
    print('A sua Passagem irá custar: R${:.2f}'.format(distancia * 0.50))
    print('Foi cobrado R$0.50 por KM')
else:
    print('A Sua Passagem irá custar: R${:.2f}'.format(distancia * 0.45))
    print('Por ser uma viagem longa, foi cobrado R$0.45 por KM')