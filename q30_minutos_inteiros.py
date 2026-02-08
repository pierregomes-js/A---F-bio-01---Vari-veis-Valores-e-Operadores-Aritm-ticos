min = int(input('Digite um valor em minutos: '))

dias = min // 1440
horas = (min % 1440) // 60
minutos_restantes = min % 60

print(f'{min}min Correspondem a {dias} dias, {horas}h e {minutos_restantes}min. ')