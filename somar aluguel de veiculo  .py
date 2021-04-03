dias=float(input('quantos dias voçê ficou com o veiculo ? : '))
km=float(input('quantos km voçê rodou com o veiculo ? : '))
diaria= 60*dias
rodagem=km*0.15
soma=diaria + rodagem
print(' voçe tem a pagar pelo aluguel do veiculo R$ {}'.format(soma))
