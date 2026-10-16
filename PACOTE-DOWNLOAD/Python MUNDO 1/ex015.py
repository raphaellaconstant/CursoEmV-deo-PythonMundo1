km = float(input('Quantos quilômetros você percorreu?'))
dias = int(input('E por quantos dias o carro foi alugado?'))
total = (km * 0.15) + (dias * 60)
print('O preço a se pagar pelo aluguel de {} dias é R${:.2f}'.format(dias,total))

