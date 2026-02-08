x1 = int(input('x do ponto 1: '))
y1 = int(input('y do ponto 1: '))

x2 = int(input('x do ponto 2: '))
y2 = int(input('y do ponto 2: '))

distancia = (((x2 - x1) **2) + ((y2 - y1) **2)) ** (1/2)

print(f'A distância dos pontos {x1},{y1} e {x2},{y2} é {distancia}.')