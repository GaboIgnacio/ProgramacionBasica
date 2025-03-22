numeros = [3, 1, 5, 7, 87777, 2, 10]
for i in range(len(numeros)):  
    if numeros[i] > 0: 
        numeros[i] = -numeros[i]  
print(numeros)  
