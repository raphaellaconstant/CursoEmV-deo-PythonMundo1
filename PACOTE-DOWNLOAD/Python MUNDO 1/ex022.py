'''Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas e minúsculas.
Quantas letras ao todo (sem considerar espaços).
Quantas letras tem o primeiro nome.'''

#n1 = input('Qual é o seu nome completo?')
#mai = n1.upper()
#min = n1.lower()
#nl = len(n1)
#pn = n1.split()
#npn = len(pn[0])
#print('''O seu nome é {}
#O nome em letras maiúsculas é {}
#O nome em letras minúsculas é {}
#Seu nome tem ao todo {} letras.'''. format(n1,mai,min,nl,n1))
#print('Seu primeiro nome é {}.'.format(pn[0]))
#print('Seu primeiro nome tem {} letras.'.format(npn))

n1 = input('Qual é o seu nome completo?').strip()
mai = n1.upper()
min = n1.lower()
nl = len(n1) - n1.count(' ')
pn = n1.split()
npn = len(pn[0])
print('''O seu nome é {}
O nome em letras maiúsculas é {}
O nome em letras minúsculas é {}
Seu nome tem ao todo {} letras.'''. format(n1,mai,min,nl,n1))
print('Seu primeiro nome é {}.'.format(pn[0]))
print('Seu primeiro nome tem {} letras.'.format(npn))





