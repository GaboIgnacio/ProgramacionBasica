# # Este código sirve para interactuar con una lista de números mediante un menú de opciones:
# 1. Agregar un número a la lista.
# 2. Borrar un número de la lista si existe.
# 3. Insertar un número en una posición específica de la lista.
# 4. Mostrar la lista actual de números.
# 5. Salir del programa.
# El programa sigue ejecutándose en un bucle hasta que el usuario elige la opción de salir.

numeros = [1, 2, 3]

while True:
    print("\n===== Bienvenido 🤡 =====")
    print("1. Agregar ")
    print("2. Borrar")
    print("3. Insertar")
    print("4. Mostrar ")
    print("5. queri salir? ")
    
    opcion = input("Elige una opción, plis: ")

    if opcion == "1":
        nuevo = int(input("Que numero Agregamos: "))
        numeros.append(nuevo)
        print("Lista actualizada:", numeros)

    elif opcion == "2":
        borrar = int(input("Que numero Borramos: "))
        if borrar in numeros:
            numeros.remove(borrar)
            print("Número borrado. Lista actualizada:", numeros)
        else:
            print("Ese número no está en la lista, loco 🤡.")

    elif opcion == "3":
        nuevo_numero = int(input("Ingresa el número a insertar oe: "))
        posicion = int(input("Ingresa en qué posición lo queri poner oe (empieza en 0): "))
        if 0 <= posicion <= len(numeros):
            numeros.insert(posicion, nuevo_numero)
            print("Número insertado. Lista actualizada:", numeros)
        else:
            print("Posición inválida, hermano.")

    elif opcion == "4":
        print("Lista actual:", numeros)

    elif opcion == "5":
        print("¡Chao pescao!")
        break

    else:
        print("Opción inválida, elige bien po.")
