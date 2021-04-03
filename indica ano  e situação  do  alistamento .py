# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual=date.today().year
nasc=int(input(' Qual o ano de seu nascimento ? :'))
idade = atual -nasc
print('quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))
nome=str(input(' Qual seu sexo ?; '))
if nome or f:
       print(' Voce não precisa se alistar ')
elif idade == 18:
       print('Vocce tem que alistar IMEDIATAMENTE !!')
elif idade < 18 :
       saldo = 18 - idade
       print ('Ainda faltam {} anos para seu alistamento '.format(saldo))
       ano=atual + saldo
       print('Seu alistamento sera em {} '.format(ano))
elif idade > 18 :
       saldo = idade- 18
       print('Voce ja deveria ter se alistado há {} anos '.format(saldo))
       ano=atual - saldo
       print(' Seu a alistamento foi em {}'.format(ano))
