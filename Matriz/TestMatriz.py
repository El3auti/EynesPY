import random

# Crear matriz 5x5 randomizada
matriz = [[random.randint(0, 9) for x in range(5)] for y in range(5)]
print("Matriz:")
for fila in matriz:
    print(fila)

# Buscar secuencia de 4 números consecutivos horizontal
for i in range(5):
    for j in range(2):
        if matriz[i][j] == matriz[i][j+1] == matriz[i][j+2] == matriz[i][j+3]:
            print(f"Secuencia horizontal encontrada en la fila {i+1} desde la columna {j+1} hasta la columna {j+4}")

# Buscar secuencia de 4 números consecutivos vertical
for i in range(2):
    for j in range(5):
        if matriz[i][j] == matriz[i+1][j] == matriz[i+2][j] == matriz[i+3][j]:
            print(f"Secuencia vertical encontrada en la columna {j+1} desde la fila {i+1} hasta la fila {i+4}")