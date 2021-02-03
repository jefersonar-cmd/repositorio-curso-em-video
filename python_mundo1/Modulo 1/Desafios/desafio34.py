# escreva um programa que pergunte o salario de um funcionário  e calcule o valor do seu aumento
# para salários superiores a R$1.250 calcule um aumento de 10%
#para os inferiores ou iguais, o aumento é de 15%
salarioant = float(input('Informe o salário atual R$'))
if salarioant > 1250:
    novo = salarioant * 0.1
    novo = salarioant + novo
    print('O salário será de R${:.2f} para R${:.2f}'.format(salarioant, novo))
elif salarioant <= 1250:
    novo = salarioant * 0.15
    novo = salarioant + novo
    print('O salário será de R${:.2f} para R${:.2f}'.format(salarioant, novo))