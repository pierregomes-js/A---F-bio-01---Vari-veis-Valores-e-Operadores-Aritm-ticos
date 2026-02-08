numero = int(input('Escreva um número de 4 dígitos: '))

milhar = numero // 1000
centena = ( numero % 1000 ) // 100
dezena = ( numero % 100 ) // 10
unidade = numero % 10

soma = milhar + centena + dezena + unidade

print(f'A soma dos dígitos do número {numero} é {soma}.')