## O mesmo professor do desafio 019 quer sortear a ordem de apresenta√ß√£o de trabalhos dos alunos. Fa√ßa um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
n1=input('nome do primeiro aluno :')
n2=input('nome do segundo aluno :')
n3=input('nome do terceiro aluno :')
n4=input('nome do quarto aluno :')
lista=[n1,n2,n3,n4]
random.shuffle(lista)
print(' a ordem de apresentaÁ„o ser„o {}'.format(lista))

