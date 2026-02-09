cotacao = float(input('Cotação do dólar: '))

valor_dolar = float(input('Digite sua quantidade de dinheiro em dólares: '))

conversao = cotacao * valor_dolar

print(f'US${valor_dolar:.2f} equivalem a R${conversao:.2f}.')