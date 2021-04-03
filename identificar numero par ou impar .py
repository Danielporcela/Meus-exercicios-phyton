#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
numero=int(input('Digite um numero :'))
resultado= numero % 2 # verificação pra ver se é par ou impar 
if resultado == 0 :
       print (' O numero {} é par '.format(numero))
else:
       print ('O numero {} é impar '.format(numero))
