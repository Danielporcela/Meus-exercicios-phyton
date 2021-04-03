#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
n1=int(input('Digite um numero :'))
n2=int(input('Digite outro numero :'))
if n1 > n2 :
       print(' o primeiro numero  [{}] é maior que o segundo [{}]'.format(n1,n2))
elif n1 < n2:
       print(' o segundo numero [{}] é maior que o primeiro [{}] '.format(n2,n1))
else:
       print(' os dois numeros [{}] [{}] saõ iguais '.format(n1,n2))
