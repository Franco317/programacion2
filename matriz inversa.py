
matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# matriz original
print("Matriz original:")
for fila in matriz:
  print(fila)

# Muestro la matriz inversa horizontalmente
print("Matriz inversa horizontalmente:")
for fila in matriz:
  fila.reverse() # Invertir el orden de los elementos de cada fila
  print(fila)
