# Este código sirve para insertar un nuevo número en una lista en una posición específica indicada por el usuario. 
# Luego muestra la lista actualizada con el número insertado en la posición deseada.

numeros = [1, 2, 3]

nuevo_numero = int(input("Ingresa el número a insertar pesao: "))
posicion = int(input("Ingresa en qué posición lo queri poner oe: "))

numeros.insert(posicion, nuevo_numero)

print(numeros)
