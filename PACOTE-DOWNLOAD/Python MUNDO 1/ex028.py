'''Escreva um programa que faça o computador "pensar" em
um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
num = int(randint(0,5))
print('Escolhi um número entre 0 e 5.')
usu = int(input('Você consegue adivinhar que número foi esse?'))
if usu == num:
    print('VOCÊ ACERTOU!')
else:
    print('Você errou. Tente novamente!')
print('O número que eu escolhi foi {}.'.format(num))

