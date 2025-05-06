#agregar numeros
numero = [1,2,3]
numeros = int(input("agrega numero boludo: "))
numero.append(numeros)
print(numero)

#borrar numero

numeros = int(input("borra numero boludo: "))
numero.remove(numeros)
print(numero)

# poner en posicion especifica

nuevo_numero = int(input("Ingresa el número a insertar pesao: "))
posicion = int(input("Ingresa en qué posición lo queri poner oe: "))

numeros.insert(posicion, nuevo_numero)

print(numeros)

# 1. Agregar un número al final de la lista `numero` mediante el uso del método `append`.
# 2. Eliminar un número específico de la lista `numero` utilizando el método `remove`.
# 3. Insertar un número en una posición específica dentro de la lista `numero` usando el método `insert`.