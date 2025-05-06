file = open ("archivo.txt","w")
file.write("hola mundo")
file.close()
with open("archivo.txt", "r") as file:
  contenido = file.read()
  print(contenido)

with open("datos.txt", "w") as files:
    files.write("hola mundo \n")
    files.write("fin \n")
print("archivo 'datos.txt' fue guardado")


with open("datos.txt", "r") as file:
    contenido = file.read()

print(contenido)

# 1. Crear un archivo llamado "archivo.txt", escribir el texto "hola mundo" en él y luego leerlo para mostrar su contenido.
# 2. Crear un archivo llamado "datos.txt", escribir dos líneas de texto ("hola mundo" y "fin"),
#  guardar el archivo y luego leer su contenido para mostrarlo en la consola.