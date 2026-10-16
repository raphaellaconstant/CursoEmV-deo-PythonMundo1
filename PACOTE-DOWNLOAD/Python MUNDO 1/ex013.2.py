prod = float(input('Digite o valor do produto:'))
vis = prod - (prod * 10/100)
parce = prod + (prod * 10/100)
print('O produto de valor R${:.2f} custa R${:.2f} pago à vista e R${:.2f} pago parcelado.'.format(prod,vis,parce))
