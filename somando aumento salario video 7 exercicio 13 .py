 #faça um programa que leia o salario de um funcionario e mostre o seu novo salario com 15% de aumento ****
salario=float(input('digite o salario do funcionario ? R$'))
soma=(salario*15/100)
aumento=salario+soma
print('um funcionario que ganhava R${}, com o aumento de 15% passa a receber R${}'.format(salario,aumento))
