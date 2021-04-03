##Crie um programa que leia o nome completo de uma pessoa e mostre: 
##- O nome com todas as letras maiúsculas e minúsculas.
##- Quantas letras ao todo (sem considerar espaços).
##- quantas letras tem o primeiro nome .
nome=str(input('Digite seu nome completo :')).strip()#função strip retira a contagem com os espaços ##3 
print(' Analisando seu nome.....')
print('Seu nome em maiuculo é {}'.format(nome.upper()))# função upper transforma letras para maiusculas #
print('Seu nome em minusculo é {}'.format(nome.lower()))#função lower transforma letras para minusculas #
print('Seu nome contem {} letras'.format(len(nome)- nome.count(' ')))# função  count conta quantas letras possui o nome digitado ##
print('O primeiro nome tem {} letras'.format(nome.find(' ')))##função find informa quantas letras tem no primeiro nome digitado ##
