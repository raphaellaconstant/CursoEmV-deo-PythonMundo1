'''import math
pre = float(input('Digite um número com quatro casas decimais:'))
num = math.trunc(pre)
print('O número {:.3f} tem a porção inteira de {}.'.format(pre,num))'''

pre = float(input('Digite um número de quatro casas decimais:'))
print('O número {} tem a porção inteira de {}.'.format(pre,int(pre)))
