#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
computador = randint (0,2 )
print(' VAMOS JOGAR JOKEMPÔ ? ')
print(' Suas opçoes :')
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
itens = ('PEDRA', 'PAPEL' ,' TESOURA ')
computador = randint(0,2)
jogador=int(input(' Qual é a sua jogada ? Digite um numero:'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!!!! ')
sleep(1)
print('==='*20)
print('Computador jogou {}'.format(itens[computador ]))
print('Jogador jogou  {}'.format(itens[jogador]))
if computador == 0:# COMPUTADOR JOGOU PEDRA 
       if  jogador ==  0:
              print (' empate ')
       elif jogador == 1 :
              print ('jogador venceu')
       elif jogador == 2:
              print ('computador venceu ') 
       else :
              print(' OPÇAO INVALIDA !!!')
elif computador == 1:# COMPUTADOR JOGOU PAPEL
       if jogador ==0: 
              print ('computador venceu ')
       elif jogador== 1:
              print ('empate ')
       elif jogador == 2 :
              print('jogador venceu ')
       else:
              print (' OPÇAO INVALIDA !!! ')
elif computador == 2 :# computador JOGOU TESOURA 
       if jogador == 0:
              print( ' jogador  venceu ')
       elif jogador == 1 :
              print ('computador  venceu') 
       elif jogador == 2 :
              print (' empate ')
       else :
              print (' OPÇAO INVALIDA !!! ')
       
print('==='*20)
