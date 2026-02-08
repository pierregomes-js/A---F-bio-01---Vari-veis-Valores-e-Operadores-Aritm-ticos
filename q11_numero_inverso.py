numero = int(input('digite um número de 3 algorismos: '))

centenas = numero // 100
dezenas = (numero % 100) // 10
unidade = numero % 10

inverso = (unidade * 100) + (dezenas * 10) + centenas

print(f'A inversão dos algarismos desse número é {inverso}.')