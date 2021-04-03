#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retrangulo , calcule e mostre o comprimento da hipotenusa#
co=float(input('digite o comprimento do cateto oposto:'))
ca=float(input('digite o comprimento do cateto adjacente :'))
soma= (co **2 + ca **2)**(1/2)
print(' A hipotenusa vai medir {:.2f}'.format(soma))
*****************************************************************************************************************************                   
#import math
co=float(input('digite o comprimento do cateto oposto :'))
ca=float(input('digite o comprimento do cateto adjento :'))
soma=math.hypot(co,ca)
print(' A hipotenusa vai medir {:.2f}'.format(soma))
**********************************************************************************************************************************


 as duas formas de criar calculo

1° usando logica simples

2° usando modulo math .hypot
