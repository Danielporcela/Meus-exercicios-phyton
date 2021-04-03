#Escreva um programa para aprovar empréstimo bancário para a compra de casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa=float(input('valor da casa :'))
salario=float(input('salario do comprador :'))
anos=int(input('quantos anos de financiamento :'))
prestaçao=casa/(anos*12 )
valor=salario * 30 /100
print('Para pagar uma casa no valor de R$ {:.2f} em {} anos'.format(casa ,anos))
print(' A prestação sera de {:.2f}'.format(prestaçao))
if prestaçao  >=valor :
       print('seu  financiamento foi negado ')
else :
       print('seu financiamento foi APROVADO!!! PARABENS')
