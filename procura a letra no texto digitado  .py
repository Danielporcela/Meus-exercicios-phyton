###Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase=str(input(' Digite uma frase :')).upper().strip()# O COMANDO UPPPER IGUAL NA CONTAGEM LETRAS MAIUCULAS E MINUSCULAS#
print(' A letra A  aparece {} vesez na frase '.format(frase.count('A')))# O COAMANDO COUNT  CONTA QUANTAS LETRAS EXISTE NA FRASE DIGITADA #
print('A letra A aparece na {} posição na primeira vez '.format(frase.find('A')+1))# O COMANDO FIND + 1 INFORMA EM QUAL POSIÇÃO COMEÇA A LETRA NA FRASE  #           
print('A ultima letra A aparece na {}posição pela ultima vez '.format(frase.rfind('A')+1)) # o comando RFIND - 1 INFORMA A ULTIMA POSIÇÃO QUE TEM  A LETRA NA FRASE# 
