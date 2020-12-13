# faça uma aplicação que leia
# um valor em metros e o exiba
# convertido em centimetros e em
# milímetros

metro = float(input('Quantos metros quer converter? '))

print('Os {} metros \nEm centímetros: {}cm \nEm milímetros: {}mm'.format(int(metro), int(metro*100), int(metro*1000)))