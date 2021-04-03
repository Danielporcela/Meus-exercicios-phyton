#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, casseno e tangente de angulo
import math
angulo=float(input(' digite um angulo que você deseja:'))
seno = math.sin(math.radians(angulo))
print('o angulo {} tem o seno de {:.2f} '.format(angulo,seno))
cosseno=math.cos(math.radians(angulo))
print(' o angulo {} tem o coseno de {:.2f}'.format(angulo,cosseno))
tangente=math.tan(math.radians(angulo))
print(' o angulo{} tem a tangente de {:.2f}'.format(angulo,tangente))
             
             
