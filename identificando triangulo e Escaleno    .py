#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferente

r1=float(input('Digite o primeiro segimento :'))
r2=float(input('Digite o segundo segmento :'))
r3=float(input('Digite o terceiro segmento :'))
if r1 < r2 + r3 and r2< r1 + r3 and r3 < r2 +r1 :
       print('Os segmentos acima PODEM FORMAR TRIANGULO ')
       if r1 == r2  == r3 :
              print('Este triangulo é do tipo EQUILÁTERO ')
       elif r1 != r2 != r3 != r1:
              print('Este triangulo é do tipo ESCALENO ')
       else:
              print(' Este triangulo é do tipo ISOSCELES ')
else:
 print('Os segmentos acima NÃO PODEM FORMAR TRIANGULO ')

