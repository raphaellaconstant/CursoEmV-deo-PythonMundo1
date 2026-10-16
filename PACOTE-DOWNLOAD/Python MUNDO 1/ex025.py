'''Exercício Python 025: Crie um programa que leia o nome de uma pessoa e
diga se ela tem "SILVA" no nome.'''

#n1 = str(input('Qual é o seu nome completo?')).strip()
#silva = n1.lower()=='silva'
#print('Seu nome tem Silva? {}'.format('Silva'.lower()in n1))

'''CORRETO:'''

n1 = str(input('Qual é o seu nome completo?'))
print('Seu nome tem Silva? {}'.format('silva' in n1.lower()))





