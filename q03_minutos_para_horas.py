minutos = int(input('digite um valor em minutos: '))

horas = minutos // 60
resto_minutos = minutos % 60

print(f'{minutos}min quivalem a {horas}h e {resto_minutos}min.')