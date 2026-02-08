anos_fumados = int(input('Digite a quantidade de anos que o fumante fuma: '))
por_dia = int(input('Digite a quantidade de cigarros fumados por dia: '))
preco_carteira = float(input('Digite um preço de uma carteira de cigarro: '))

anos_dias = anos_fumados * 365
total_cigarros = anos_dias * por_dia
valor = (total_cigarros / 20) * preco_carteira

print(anos_dias, total_cigarros, valor)