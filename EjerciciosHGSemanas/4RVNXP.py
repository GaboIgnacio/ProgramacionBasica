# Reemplazar Valores Negativos por su contraparte positiva
numeros = [-3, 1, 5, -7, 8, -2, -10, 20, -255]
for i in range(len(numeros)): 
    if numeros[i] < 0:  
        numeros[i] = -numeros[i]  

print(numeros)  
