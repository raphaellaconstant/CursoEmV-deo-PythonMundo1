'''Faça um programa que leia três números e mostre qual é o
maior e qual é o menor.'''

a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O maior número é {}'.format(maior))
print('O menor número é {}.'.format(menor))

