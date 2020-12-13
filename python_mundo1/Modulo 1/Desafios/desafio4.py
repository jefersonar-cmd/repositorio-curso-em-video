n = input('Digite Algo: ')

print('O tripo primitivo do texto tal foi: ', type(n))
print('O texto é composto só de espaços? ', n.isspace())
print('O texto é composto de alpha numérico? ', n.isalpha())
print('O texto é composto só de números? ', n.isalnum())
print('O texto é contém número decimal? ', n.isdecimal())
