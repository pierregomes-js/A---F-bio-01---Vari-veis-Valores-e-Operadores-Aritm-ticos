m = int(input('Digite um valor inteiro de metros: '))

km = m // 1000
metros_restantes = m % 1000

print(f'{m}m Correspondem a {km}km e {metros_restantes}m.')