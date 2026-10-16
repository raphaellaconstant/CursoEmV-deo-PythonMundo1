larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
area = larg * alt
print('Sua parede de {} de largura e {} de altura tem a área de {}m²'.format(larg,alt,area))
tinta = area/2
print('Para pintar sua parede, você precisará de {} litros de tinta'.format(tinta))
