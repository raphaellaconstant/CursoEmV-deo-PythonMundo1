'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

vel = int(input('Qual a velocidade do carro?'))
if vel > 80:
    print('Atenção, você foi multado. Sua velocidade é de {}km/h, mas não é permitido ultrapassar a velocidade de 80km/h.'.format(vel))
    multa = (vel - 80) * 7
    print('Sua multa equivale a R${:.2f}.'.format(multa))
else:
    print('Pode seguir. Dirija com segurança!')


