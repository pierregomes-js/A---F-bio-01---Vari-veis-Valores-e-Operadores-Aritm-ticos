dias = int(input('Digite sua idade expressa em dias: '))

anos = dias // 365
meses = (dias % 365) // 30
dias_restantes = meses % 30

print(f'{dias} Dias equivalem a {anos} anos, {meses} meses e {dias_restantes} dias.')