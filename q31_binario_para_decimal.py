binario = int(input('digite um número binário de 4 algarismos: '))

milhar = binario // 1000
centena = ( binario % 1000 ) // 100
dezena = ( binario % 100 ) // 10
unidade = binario % 10

decimal = ((milhar * (2 ** 3)) + (centena * (2 ** 2)) + (dezena * 2) + unidade)

print(f'{binario} em casa decimal equivalem a {decimal}.')