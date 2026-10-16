'''Faça um programa que leia uma frase pelo teclado
e mostre quantas vezes aparece a letra "A", em que posição ela aparece
a primeira vez e em que posição ela aparece a última vez.'''

#frase = str(input('Digite uma frase:')).strip()
#print('Na sua frase, a letra A aparece {} vezes.'.format(frase.lower().count('a')))
#print('A primeira letra A apareceu na posição {}.'.format(frase.lower().find('a')))
#print('A última letra A apareceu na posição {}.'.format(frase.lower().))

frase = str(input('Digite uma frase:')).strip()
print('Na sua frase, a letra A aparece {} vezes.'.format(frase.lower().count('a')))
print('A primeira letra A apareceu na posição {}.'.format(frase.lower().find('a')+1))
print('A última letra A apareceu na posição {}.'.format(frase.lower().rfind('a')+1))
