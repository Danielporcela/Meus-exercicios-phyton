##Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num=int(input(' digite um numero :'))
u=num // 1 % 10
d=num // 10 % 10
c=num // 100 % 10
m=num // 1000 % 10 
print('analisando o numero {}'.format(num))           
print('Possui {} unidades'.format(u))
print('Possui {} dezenas'.format(d))
print('Possui {} centenas'.format(c))
print('Possui {} milhar'.format(m))
