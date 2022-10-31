matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for c, coluna in enumerate(matriz):
    for l, linha in enumerate(coluna):
        matriz[c][l] = (int(input(f'Digite um valor para [{c}, {l}]: ')))

print('-='*30)

for c, coluna in enumerate(matriz):
    for l, linha in enumerate(coluna):
        print(f'[{matriz[c][l]:^5}]', end='')
    spar += matriz[l][c]
    print()
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'a soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')