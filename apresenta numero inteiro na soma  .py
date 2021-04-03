#crie um programa que leia um numero real  qualquer pelo teclado e mostre na tela a sua porção inteira

import math
num=float(input('digite um numero :'))
inteiro=math.trunc(num)
print('numero digitado {} tem a parte  inteira {}'.format(num,inteiro))
