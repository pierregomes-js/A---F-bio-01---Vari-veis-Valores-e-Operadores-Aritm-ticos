numero = int(input('digite um número de 3 algarismos: '))

centenas = numero // 100
dezenas = (numero % 100) // 10
unidade = numero % 10

somatorio = centenas + dezenas + unidade

print(f'A soma dos algarismos do número é {somatorio}.')