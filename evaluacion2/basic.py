# Escribir en archivo.txt
file = open("archivo.txt", "w")
file.write("hola mundo")
file.close()

# Leer archivo.txt
with open("archivo.txt", "r") as file:
    contenido = file.read()
    print(contenido)

# Escribir en datos.txt
with open("datos.txt", "w") as files:
    files.write("hola mundo \n")
    files.write("fin \n")

print("archivo 'datos.txt' fue guardado")