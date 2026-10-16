''' Faça um programa que leia o nome completo de uma pessoa, mostrando
em seguida o primeiro e o último nome separadamente.'''

#p1 = str(input('Qual é o seu nome completo?'))
#n1 = p1.split()
#n2 = p1.rsplit()
#print('Muito prazer em te conhecer!')
#print('Seu primeiro nome é {}.'.format(n1[0]))
#print('Seu último nome é {}.'.format(n2[0]))

p1 = str(input('Qual é o seu nome completo?')).strip()
n1 = p1.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(n1[0]))
print('Seu último nome é {}.'.format(n1[-1]))
