salario = float(input('Qual é o salario do funcionario ? R$ '))
aumento = salario + (salario *15 / 100)
print(' Um funcionario que ganhava R$ {:.2f}, com aumento de 15 % passa a receber R$ {:.2f} '.format(salario,aumento ))
