'''Faça um programa que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento
da hipotenusa.'''

'''Obs: O quadrado da hipotenusa é igual à soma dos quadrados dos catetos.
Então a hipotenusa é a raiz quadrada da soma dos quadrados dos catetos.'''

'''co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

'''AGORA IMPORTANDO UMA BIBLIOTECA:'''

from math import hypot
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))






