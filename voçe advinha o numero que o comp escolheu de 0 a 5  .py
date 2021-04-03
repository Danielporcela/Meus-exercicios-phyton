#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep # tempo pra aparecer resultado 
computador=randint(0,5) #faz o computador "pensar" (0,5) numero que estipulou pra maquina pensar no maximo ate 5
#print(' pensei no numero {}'.format(computador))#### serve para testar se esta correto o numero que o computador selecionou
print('=.='*20)
print('Vou pensar em um numero de 0 ate 5 .tente advinhar ..... ')
print('=.='*20)
jogador =int(input('Digite um numero :'))#jogador tentando advinhar
print('Precessando .....')
sleep(5)#pra informar quantos segundo pra dar o resultado na tela 
if jogador == computador:
       print('Parabens voçe acertou e me venceu !')
else:
       print('Ganhei !!!!! Eu pensei no {} e voçe imformou {} tente outra vez porque eu venci desta vez kkkkkkkk '.format(computador , jogador))#resultador do jogo
