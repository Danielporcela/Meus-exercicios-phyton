# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
n1=float(input(' Digite a primeiro nota :'))
n2=float(input('Digite a segunda nota :'))
m = (n1+n2) /2
if m >= 7.0 :
       print('PARABENS VOÇE FOI APROVADO com a media {}'.format(m))
elif  6.9 > m >= 5 :
       print (' Tirando {} e {} , a media do aluno é  {}'.format(n1,n2,m))
       print (' O ALUNO ESTA EM RECUPERAÇÃO .' )
elif m < 5 :
       print (' Tirando {} e {} , a media do aluno é  {}'.format(n1,n2,m))
       print ('O ALUNO ESTA REPROVADO ')
