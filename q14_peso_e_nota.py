nota1 = float(input('primeira nota: '))
peso1 = float(input('peso da primeira nota: '))

nota2 = float(input('segunda nota: '))
peso2 = float(input('peso da segunda nota: '))

nota3 = float(input('terceira nota: '))
peso3 = float(input('peso da terceira nota: '))

media_ponderada = ((nota1 * peso1) + (nota2 * peso2) + (nota3 + peso3)) / (peso1 + peso2 + peso3)

print(f'A média ponderada das notas é {media_ponderada}.')