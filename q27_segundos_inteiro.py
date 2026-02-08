S = int(input('Digite um valor em segundos: '))

H = S // 3600
Min = (S % 3600) // 60
segundos_restantes = S % 60

print(f'{S}s equivalem a {H}h, {Min}min e {segundos_restantes}s.')