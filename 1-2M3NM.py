import numpy as np
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
resultado = matriz[0, 0] * matriz[1, 1] * matriz[2, 2]
print("La multiplicación de estos números es:", resultado)

#2da Opcion

import numpy as np
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
numero_1 = matriz[0, 2] 
numero_2 = matriz[2, 1]
numero_3 = matriz[2, 2] 

resultado = numero_1 * numero_2 * numero_3
print("La multiplicación de estos números es:", resultado)
