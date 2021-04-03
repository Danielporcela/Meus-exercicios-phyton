#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade=float(input('qual a velocidade do seu carro ?:'))
if velocidade >=81 :
       print('Multado !!Voçe excedeu o limite de velocidade permitido que é de 80K/h')
       multa= (velocidade - 80) * 7 #calculo da multa com valor por km excedente de R$7,00
       print(' A multa a pagar é de R${:.2f}'.format(multa))
print (' Tudo traquilo voçe esta dentro do limite de velocidade que é 80 K/h')

