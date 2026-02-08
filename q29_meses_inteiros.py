meses = int(input('Digite uma quantidade de meses: '))

anos = meses // 12
meses_restantes = meses % 12

print(f'{meses} Meses equivalem a {anos} anos e {meses_restantes} meses.')