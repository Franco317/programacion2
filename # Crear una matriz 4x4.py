# Creo la matriz 4x4
matriz = [[0 for j in range(4)] for i in range(4)]

for i in range(4):
    for j in range(4):
        matriz[i][j] = i * 4 + j + 1
print("Matriz:")
for i in range(4):
    for j in range(4):
        print(matriz[i][j], end="\t")
    print()

# Calcular la suma de la diagonal y la contra diagonal
suma_diagonal = 0
suma_contra_diagonal = 0
for i in range(4):
    suma_diagonal += matriz[i][i]
    suma_contra_diagonal += matriz[i][3 - i]

print("Suma de la diagonal:", suma_diagonal)
print("Suma de la contra diagonal:", suma_contra_diagonal)
