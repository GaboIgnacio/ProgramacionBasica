import numpy as np
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
for fila in matriz:
    for num in fila:
        if num > 1: 
            es_primo = True
            for i in range(2, num):
                if num % i == 0:
                    es_primo = False
                    break
            if es_primo:
                print(num, "es PRIMO")
