#faca um programa que leia um ano qualquer e mostre se ele é BISSEXTO
print('{:=^30}'.format('Verificador de Ano Bissexto'))
ano = int(input('Informe o ano atual: '))
if ano == 2012 or ano == 2016 or ano == 2020 or ano == 2024:
    print('Este ano é Bissexto!')
else:
    print('Este ano não é Bissexto!')