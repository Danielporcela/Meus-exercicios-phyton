preço = float(input(' qual é o preço do produto?  R$ '))
soma = preço * 5 / 100
desconto = preço -soma
print('o produto que custava R$ {:.2f} com o desconto de 5% vai custar R${:.2f}'.format(preço,desconto))
