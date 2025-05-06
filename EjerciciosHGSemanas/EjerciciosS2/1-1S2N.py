# Sumar dos numero dentro de una matriz
import numpy as np 
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
resultado = matriz[1,1] + matriz[2,2]
print("La suma de estos numeros:", resultado)

#2da Opcion 

import numpy as np
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
numero_1 = matriz[0, 1]
numero_2 = matriz[2, 2]

suma = numero_1 + numero_2
print("La suma de", numero_1, "y", numero_2, "es:", suma)
