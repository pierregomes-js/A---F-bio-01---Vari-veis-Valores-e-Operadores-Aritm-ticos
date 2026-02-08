anos = int(input('Escreva dua idade expressa em anos: '))
meses = int(input('Meses restantes: '))
dias = int(input('Dias restantes: '))

anos_dias = anos * 365
meses_dias = meses * 30

total = anos_dias + meses_dias + dias

print(f'{anos} anos, {meses} meses e {dias} dias equivalem a {total} dias.')