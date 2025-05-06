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

# 1. Escribir el texto "hola mundo" en un archivo llamado "archivo.txt".
# 2. Leer el contenido de "archivo.txt" y mostrarlo en la consola.
# 3. Escribir dos líneas de texto ("hola mundo" y "fin") en un archivo llamado "datos.txt" y luego informar que el archivo fue guardado.
