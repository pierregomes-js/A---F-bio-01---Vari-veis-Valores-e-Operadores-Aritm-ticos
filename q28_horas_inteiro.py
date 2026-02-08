horas = int(input('Digite um valor em horas: '))

semanas = horas // 168
dias = (horas % 168) // 24
horas_restantes = horas % 24

print(f'{horas}h Correspondem a {semanas} semanas, {dias} dias e {horas_restantes}h. ')