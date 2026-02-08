n1 = int(input('numerador da primeira fração: '))
d1 = int(input('denominador da primeira fração: '))
n2 = int(input('numerador da segunda fração: '))
d2 = int(input('denominador da segunda fração: '))

numerador = (n1 * d2) + (d1 * n2)
denominador = d1 * d2

print(f'{n1}/{d1} + {n2}/{d2} = {numerador}/{denominador}')