##031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input('Digite o km da viagem :'))
print('Você esta preste a começar uma viagem de {:.1f}km'.format(km))
if km <=200:
       curta = km * 0.50
       print(' O preço desta viagem ira custar R$ {:.2f}'.format(curta))
else :
       longa = km * 0.45
       print (' O preço desta viagem ira custar R$ {:.2f}'.format(longa))
             
