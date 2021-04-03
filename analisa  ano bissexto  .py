##032: Faça um programa que leia um ano qualquer e mostre se ele não é bissexto.
from datetime import date
ano=int(input(' Que ano quer analisar ? COLOQUE 0 para analisar  ano atual : '))
if  ano == 0:
       ano = date .today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
       print (' O ano {} o ano Ã© BIXESTO '.format(ano))
else :
       print (' O ano {} NÃƒO Ã‰ BISSEXTO'.format(ano))
