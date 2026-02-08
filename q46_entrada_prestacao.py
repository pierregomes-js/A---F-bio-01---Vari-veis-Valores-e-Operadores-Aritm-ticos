valor_mercadoria = float(input('Informe o valor da mercadoria: '))

prestacoes = valor_mercadoria // 3
entrada = prestacoes + (valor_mercadoria % 3)

print(f'A entrada do produto é R${entrada} e as duas prestações iguais são R${prestacoes}')