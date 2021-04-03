#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
from datetime import date
atual=date .today().year
nasc=int(input(' Qual ano de seu nascimento ? :'))
idade=atual-nasc
print('Voçe tem {:.1f} anos '.format(idade))
if idade <=9:
       print(' com idade de {} anos voce esta na categoria mirin '.format(idade))
elif idade <=14:
       print(' Voce esta na categoria infantil ')
              
elif idade <= 19:
       print(' Voce esta na categoria junior ')
elif idade <= 25 :
       print(' Voce esta na categoria senior ')
else:
       print (' Voce esta na categoria  master ')
       
             
