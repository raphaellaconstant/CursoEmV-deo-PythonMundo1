'''Desenvolva um programa que pergunte a distância de uma
viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km
para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

via = int(input('Qual a distância da sua viagem?'))
if via <= 200:
    pre1 = via * 0.50
    print('O preço da sua passagem será de R${:.2F}.'.format(pre1))
else:
    pre2 = via * 0.45
    print('O preço da sua passagem será de R${:.2f}.'.format(pre2))
