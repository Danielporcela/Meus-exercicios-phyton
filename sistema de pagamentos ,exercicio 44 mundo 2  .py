#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal 

#– 3x ou mais no cartão: 20% de juros#
print('================== LOJA ASAPH =================== ')
preço=float(input(' Digite o preço das compras :'))
print('''QUAL A FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ou mais''')
opçao=int(input(' Qual é a opção ? '))
if opçao == 1 :
       total = preço -(preço *10/100)
elif opçao == 2 :
       total = preço - (preço * 5 /100)
elif opçao == 3 :
      total = preço 
      parcela = total /2
      print(' sua coma ira ser parcelaa em 2x de {:.2f}'.format(parcela))
elif opçao == 4 :
       total =  preço + (preço *20 /100) 
       parcela = total / 3
       print(' sua coma ira ser parcelaa em 3x de {:.2f}'.format(parcela)) 
print(' Sua compra no valor de R${}  ira ficar no total de R$ {:.2f} '.format(preço,total))
