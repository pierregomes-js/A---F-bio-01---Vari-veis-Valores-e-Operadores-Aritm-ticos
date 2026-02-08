valor = int(input('informe o valor que deseja realizar saque: '))

cinquenta = valor // 50
dez = (valor % 50) // 10
cinco = (valor % 10) // 5
um = valor % 5

print(cinquenta, dez, cinco, um)