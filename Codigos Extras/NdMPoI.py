# Analiza si los números de una matriz 3x3 son pares o impares y los imprime uno por uno con su clasificación.
import numpy as np
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
numeros = [matriz[0, 0], matriz[0, 1], matriz[0, 2], matriz[1, 0], matriz[1, 1], matriz[1, 2],matriz[2, 0],matriz[2, 1],matriz[2, 2]]
for num in numeros:
    if num % 2 == 0: 
        print(f"{num} es PAR")
    else:
        print(f"{num} es IMPAR")
