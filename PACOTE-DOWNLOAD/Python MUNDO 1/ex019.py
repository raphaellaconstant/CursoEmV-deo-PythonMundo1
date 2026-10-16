'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome
escolhido.'''

'''import random
a1 = input('O primeiro aluno:')
a2 = input('O segundo aluno:')
a3 = input('O terceiro aluno:')
a4 = input('O quarto aluno:')
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))'''

'''PARA SER MAIS OBJETIVO:'''

from random import choice
a1 = input('O primeiro aluno:')
a2 = input('O segundo aluno:')
a3 = input('O terceiro aluno:')
a4 = input('O quarto aluno:')
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))




