# faça um programa que leia um angulo qualquer  mosre na tela o valor do seno, cosseno e tangente desse angulo

import math
ang = float(input('Digite o Ângulo que você deseja: '))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O seno {:.2f}, o cosseno {:.2f} e o tangente {:.2f}, do ângulo {}'.format(sen, cos, tan, ang))