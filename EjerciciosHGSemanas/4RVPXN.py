# # Este código sirve para recorrer una lista de números y cambiar los valores positivos a negativos. 
# Si el número es mayor que 0, se convierte en su versión negativa.
numeros = [3, 1, 5, 7, 87777, 2, 10]
for i in range(len(numeros)):  
    if numeros[i] > 0: 
        numeros[i] = -numeros[i]  
print(numeros)  
