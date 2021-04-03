##Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a=int(input('Digite o valor :'))
b=int(input('Digite o segundo valor :'))
c=int(input(' Digite o terceiro valor :'))
#verificando quem é o menor #
menor = a
if b<a and b<c :
       menor =b
if c<a and c<b :
       menor =c
if a<b and a<c :
       menor = a
if b  >a and b>c :
       maior = b
if c>b and c>a:
       maior = c
print(' O menor valor é {}'.format(menor))
print(' O maior valor é {}'.format(maior))
       
