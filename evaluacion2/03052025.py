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
