# Este código sirve para recorrer e imprimir todos los elementos de una matriz 3x3 en orden fila por fila,
#  mostrando los números en una sola línea separados por espacios.
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for fila in matriz: 
    for elemento in fila: 
        print(elemento, end=" ")