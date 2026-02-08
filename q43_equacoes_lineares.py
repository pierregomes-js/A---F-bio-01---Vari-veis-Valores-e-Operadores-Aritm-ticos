a = int(input('Coeficiente a: '))
b = int(input('Coeficiente b: '))
c = int(input('Coeficiente c: '))
d = int(input('Coeficiente d: '))
e = int(input('Coeficiente e: '))
f = int(input('Coeficiente f: '))

x = ((c * e) - (b * f)) / ((a * e) - (b * d))
y = ((a * f) - (c * d)) / ((a * e) - (b * d))

print(f'x = {x} , y = {y}.')