#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

#– IMC abaixo de 18,5: Abaixo do Peso

#– Entre 18,5 e 25: Peso Ideal

#– 25 até 30: Sobrepeso

#– 30 até 40: Obesidade

#– Acima de 40: Obesidade Mórbida

peso=float(input(' Digite seu pesso :'))
altura=float(input('Digite sua altura :'))
imc= peso /(altura**2) 
print(' seu IMC é {:.1f} '.format (imc))
if imc <18.5 :
       print(' Voce esta abaixo do peso ')
elif imc <=25:
       print('Voce esta no peso ideal ')
elif imc <=30 :
       print(' Voce esta com VOCE ESTA COM SOBRE PESO ')
elif imc <40:
       print ('Voce esta em ESTADO DE OBESIDADE ')
else :
       print ('OBESIDAE MORBIDA  ')
