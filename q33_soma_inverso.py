numero = int(input('digite um número de 3 algarismos: '))

centenas = numero // 100
dezenas = (numero % 100) // 10
unidade = numero % 10

inverso = (unidade * 100) + (dezenas * 10) + centenas
soma = numero + inverso

print(f'A soma do número {numero} e seu inverso ({inverso}) é {soma}.')