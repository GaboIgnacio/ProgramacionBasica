import numpy as np
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
numero_1 = matriz[0, 0] 
numero_2 = matriz[0, 1]  
numero_3 = matriz[0, 2]  
numero_4 = matriz[1, 0]  
numero_5 = matriz[1, 1]  
numero_6 = matriz[1, 2]  
numero_7 = matriz[2, 0]  
numero_8 = matriz[2, 1] 
numero_9 = matriz[2, 2] 
for num in [numero_1, numero_2, numero_3, numero_4, numero_5, numero_6, numero_7, numero_8, numero_9]:
    if num % 2 == 0:
        print(num, "es PAR")
    else:
        print(num, "es IMPAR")

#2da Opcion        

import numpy as np
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
numeros = [
    matriz[0, 0],  
    matriz[0, 1],  
    matriz[0, 2],  
    matriz[1, 0],  
    matriz[1, 1],  
    matriz[1, 2],  
    matriz[2, 0],  
    matriz[2, 1],  
    matriz[2, 2]   
]
for num in numeros:
    if num % 2 == 0: 
        print(f"{num} es PAR")
    else:
        print(f"{num} es IMPAR")
