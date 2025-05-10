# Gabriel Melo 
# Seccion: 1 (Ingeniería en Informatica y Ciberseguridad) IpLosLeones

# Aquí importamos el módulo 're' que se usa para trabajar con expresiones regulares.
import re
# Lo necesitaremos más adelante para validar que las direcciones MAC estén en el formato correcto (AA:BB:CC:DD:EE:FF).
#----------------------------------------------------------------------------------------------------------------------------------------------------------

# En esta parte creamos una lista llamada 'datos' que contiene datos de ejemplo.
# Utilizamos una lista de listas para almacenar y manipular los datos de manera más fácil.
datos = [
    ["192.168.1.2", "AA:BB:CC:DD:EE:FF", "10.0.0.2", 80, "TCP", "Permitido"],
    ["172.167.168.244", "24:01:20:02:20:25", "192.168.0.2", 443, "UDP", "Denegado"]
]
# Esta estructura nos permite acceder rápidamente a los elementos y también agregar o eliminar registros completos por su índice o ID, 
# sin tener que trabajar dato por dato, lo que hace el manejo mucho más sencillo.
# Cada sublista funciona como una fila que contiene datos: IP de origen, dirección MAC, IP de destino, puerto, protocolo y estado (Permitido o Denegado).

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Esta función se encarga de validar una dirección IP ingresada por el usuario.
def validar_ip(mensaje):
    while True: # Iniciamos un bucle infinito que se repetirá hasta que el usuario escriba una IP válida.
        ip = input(mensaje) # Pedimos al usuario que escriba una IP
        octetos = ip.strip().split(".")# Usamos .strip para eliminar espacios en blanco al principio o final.
        # Usamos .split(".") para dividir la IP en partes(octetos), usando el punto como separador.
        if len(octetos) == 4 and all(o.isdigit() for o in octetos): # Verificamos si hay exactamente 4 octetos y que todos sean dígitos (números)
            octetos = list(map(int, octetos)) # Convertimos cada octeto a número entero (de str a int) para poder compararlos.
            if 1 <= octetos[0] <= 255 and all(0 <= o <= 255 for o in octetos[1:3]) and octetos[3] != 0:
            # Aqui Validamos lo siguiente:
            #  1 <= octetos[0] <= 255 -Valida el primer octeto debe estar entre 1 y 255 (evitamos 0 porque no es válido para host comunes)
            # all(0 <= o <= 255 for o in octetos[1:3]) -Valida El segundo y tercer octeto deben estar entre 0 y 255 (cualquier valor válido en IPv4)
            # and octetos[3] != 0: Valida que el último octeto no puede ser 0 
                return ip # Si pasa todas las validaciones, retornamos la IP válida como string
        # Si algun octeto falla mostramos un mensaje al usuario y el bucle vuelve a pedir una IP
        print("❌ IP inválida. Asegúrate de que tenga 4 números separados por puntos " \
        "El primero entre 1 y 255, los del medio entre 0 y 255, y el último distinto de 0.")

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Función para validar una dirección MAC ingresada por el usuario.
def validar_mac():
    while True: # Iniciamos un bucle infinito que se repetirá hasta que el usuario escriba una MAC válida.
        mac = input("Ingrese MAC (formato AA:BB:CC:DD:EE:FF): ").upper()  # Solicitamos la MAC al usuario y la convertimos a mayúsculas con .upper().
# Verificamos si la MAC sigue el formato deseado
        if re.match("^([0-9A-F]{2}:){5}[0-9A-F]{2}$", mac):
        # 1. ^ : indica el inicio de la cadena.
        # 2. [0-9A-F]{2} : representa un par hexadecimal (dígitos del 0-9 y letras A-F, dos caracteres).
        # 3. : : es el **separador de dos puntos** entre cada par de caracteres.
        # 4. (...) : agrupa el patrón del par hexadecimal con el separador.
        # 5. {5} : repite la agrupación anterior exactamente 5 veces lo que da lugar a "AA:BB:CC:DD:EE:".
        # 6. [0-9A-F]{2} : representa el último par hexadecimal sin el dos puntos al final.
        # 7. $ : indica el final de la cadena, no debe haber más texto después.
        # Este patrón asegura que la MAC sea algo como: "AA:BB:CC:DD:EE:FF".
            return mac  # Si cumple con el formato, retornamos la MAC válida
# Si no cumple con el formato, mostramos un mensaje de error y el bucle vuelve a pedir la MAC
        print("❌ Dirección MAC inválida. Asegúrate de escribirla en el formato AA:BB:CC:DD:EE:FF.")

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Función para validar puerto
def validar_puerto():
    while True:  # Iniciamos un bucle infinito que se repetirá hasta que el usuario escriba un puerto válido.
        puerto = input("Ingrese Puerto (1-65535): ")  # Solicitamos al usuario que ingrese un puerto entre 1 y 65535
        # Verificamos que la entrada sea un número entero (sin letras ni símbolos)
        if puerto.isdigit():  # La función .isdigit() comprueba si la cadena contiene solo dígitos.
            puerto = int(puerto)  # Convertimos la cadena de texto a un número entero.
            if 1 <= puerto <= 65535: # Validamos que el puerto esté dentro del rango permitido (1-65535).
                return puerto # Si el puerto está dentro del rango válido, lo retornamos y salimos de la función.
        # Si el puerto no es válido (no es un número o está fuera del rango), mostramos un mensaje de error.
        print("❌ Puerto inválido. Recuerda que debe estar entre 1 y 65535.")  

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Función para elegir tipo de protocolo
def elegir_protocolo():
    opciones = ["TCP", "UDP", "ICMP", "ALL"]  # Definimos las opciones válidas para los protocolos
    while True:  # Iniciamos un bucle infinito, que se repetirá hasta que el usuario ingrese una opción válida
        proto = input("Ingrese protocolo (TCP/UDP/ICMP/ALL): ").upper()  # Pedimos al usuario que ingrese el protocolo y lo convertimos a mayúsculas
        if proto in opciones:  # Verificamos si el valor ingresado está en la lista de opciones válidas
            return proto  # Si el protocolo es válido, lo retornamos
        print("❌ Opción inválida. Elige entre TCP, UDP, ICMP o ALL.") # Si la opción no es válida, mostramos un mensaje de error

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Función para elegir si se permite o no
def permitido_denegado():
    opciones = ["PERMITIDO", "DENEGADO"] # Definimos las opciones válidas
    while True: # Iniciamos un bucle infinito, que se repetirá hasta que el usuario ingrese una opción válida
        valor = input("¿Permitido o Denegado?: ").upper()  # Pedimos al usuario que ingrese su respuesta y la convertimos a mayúsculas
        if valor in opciones:  # Verificamos si la respuesta está en la lista de opciones válidas
            return valor.capitalize()  # Devolvemos la respuesta en formato capitalize: esto hace que la palabra quede con la primera letra en mayúscula y el resto en minúsculas ("Permitido" o "Denegado")
        print("❌ Opción inválida. Elige entre PERMITIDO o DENEGADO.") # Si la respuesta no está en las opciones válidas, mostramos un mensaje de error
#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Función para mostrar todos los datos almacenados de forma ordenada en tabla
def mostrar_datos():
    print("\nDatos almacenados:")  # Título de la sección
    print("=" * 100)  # Línea separadora decorativa
# Mostramos los encabezados de las columnas, cada uno con un ancho fijo para que queden alineados visualmente como una tabla
    print(f"{'ID':<3}| {'IP Origen':<17} | {'MAC':<19} | {'IP Destino':<17} | {'Puerto':<7} | {'Protocolo':<9} | {'Estado'}")
    print("=" * 100)  # Línea separadora decorativa
# f es f-string, que permite insertar variables o textos con formato dentro de una cadena
# {'Texto':<N} alinea el texto a la izquierda y reserva N espacios para mantener todo ordenado como tabla.
# Así se asegura que todos los datos en las filas siguientes queden bien alineados debajo de su columna correspondiente.
    # Recorremos la lista 'datos' y mostramos cada registro formateado en columnas
    for i, d in enumerate(datos):  # 'i' es el índice (ID) del dato, 'd' es una lista con los datos
# Aquí se imprimen los datos en filas, con el mismo orden y formato usado en los encabezados de columna, alineando todo para que se vea como una tabla.
        print(f"{i:<3}| {d[0]:<17} | {d[1]:<19} | {d[2]:<17} | {str(d[3]):<7} | {d[4]:<9} | {d[5]}")
    print("=" * 100)  # Línea final decorativa para cerrar la tabla

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Función para agregar un nuevo registro a la lista de datos
def agregar():
    print("Agregando nuevo registro:")  # Indicamos al usuario que se está iniciando el proceso de ingreso
    # Se solicitan y validan uno a uno los datos necesarios
    ip_origen = validar_ip("Ingrese IP de Origen: ")      # Validamos IP de origen
    mac = validar_mac()                                   # Validamos dirección MAC
    ip_destino = validar_ip("Ingrese IP de Destino: ")    # Validamos IP de destino
    puerto = validar_puerto()                             # Validamos el puerto
    protocolo = elegir_protocolo()                        # Se elige el protocolo (TCP/UDP/etc.)
    estado = permitido_denegado()                         # Se elige si está permitido o denegado
    datos.append([ip_origen, mac, ip_destino, puerto, protocolo, estado])
    # Guardamos todos los datos en una lista.
    print("✅ Registro agregado exitosamente.") # Confirmamos que el registro se guardó

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Función para eliminar un dato de la lista por su ID
def eliminar():
    mostrar_datos()  # Mostramos todos los datos actuales para que el usuario pueda verlos y seleccionar el ID a eliminar.
    while True:  # Iniciamos un bucle que se repetirá hasta que se elimine el dato correctamente
        id_eliminar = input("Ingrese ID del dato a eliminar: ")  # Solicitamos al usuario el ID del dato que quiere eliminar
        if id_eliminar.isdigit(): # Verificamos que el ID ingresado sea un número.
            id_eliminar = int(id_eliminar)  # Convertimos la entrada a un número entero
            if 0 <= id_eliminar < len(datos): # Verificamos que el ID esté dentro del rango de datos existentes
                datos.pop(id_eliminar)  # Eliminamos el dato en la posición indicada por el ID
                print("✅ Dato eliminado correctamente.")  # Confirmamos que el dato se ha eliminado
                break  # Salimos del bucle, ya que la eliminación fue exitosa
            else:
                print("❌ ID fuera de rango.")  # Si el ID está fuera del rango de los datos, mostramos un error
        else:
            print("❌ ID inválido.")  # Si el ID no es un número válido, mostramos un error

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Función para agregar un nuevo dato en una posición específica de la lista
def agregar_en_posicion():
    mostrar_datos()  # Mostramos todos los datos actuales para que el usuario pueda ver las posiciones
    while True:  # Iniciamos un bucle que se repetirá hasta que se agregue el dato correctamente
        id_insertar = input("Ingrese posición donde desea insertar: ")  # Solicitamos al usuario la posición donde quiere insertar el nuevo dato
        if id_insertar.isdigit():  # Verificamos que la posición ingresada sea un número
            id_insertar = int(id_insertar)  # Convertimos la entrada a un número entero
            if 0 <= id_insertar <= len(datos): # Verificamos que la posición esté dentro del rango de los datos (incluido el final)
                # Solicitamos los detalles del nuevo dato
                ip_origen = validar_ip("Ingrese IP de Origen: ") # Validamos IP de origen
                mac = validar_mac()  # Validamos la dirección MAC
                ip_destino = validar_ip("Ingrese IP de Destino: ") # Validamos IP de destino
                puerto = validar_puerto()  # Validamos el puerto
                protocolo = elegir_protocolo()  # Elegimos el protocolo
                estado = permitido_denegado()  # Validamos si es permitido o denegado
                # Insertamos el nuevo dato en la posición seleccionada
                datos.insert(id_insertar, [ip_origen, mac, ip_destino, puerto, protocolo, estado])
                print("✅ Dato insertado correctamente.")  # Confirmamos que el dato se ha insertado correctamente
                break  # Salimos del bucle, ya que el dato ha sido agregado
            else:
                print("❌ Posición fuera de rango.")  # Si la posición está fuera del rango válido de índices
        else:
            print("❌ Posición inválida.")  # Si la entrada no es un número válido

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Función principal con menú de opciones
def menu():
    while True:  # Iniciamos un bucle infinito para mantener el menú activo hasta que el usuario elija salir
        print("\n  ¡Es hora de ponerte a trabajar! 🤡") # Mostramos el título del menú
        print("    Elige una opción para empezar.    ") # Mostramos el título del menú
        print("\n") # Salto de línea 
        print("  1. Agregar dato nuevo")  # Opción para agregar un nuevo dato a la lista
        print("  2. Eliminar dato por ID")  # Opción para eliminar un dato usando su ID
        print("  3. Agregar dato en posición específica")   # Opción para insertar un dato en una ubicación específica
        print("  4. Ver datos almacenados")  # Opción para ver todos los datos guardados
        print("\nPara salir del programa escribe 'terminar' cuando se te pida una opción.") # Mensaje para terminar
        print("\n")
# Pedimos al usuario que elija una opción. .strip() limpia espacios, .lower() convierte a minúscula para evitar errores.
        opcion = input("Seleccione una opción: ").strip().lower()
# Comprobamos la opción seleccionada por el usuario y ejecutamos la función correspondiente
        if opcion == "1":  # Si la opción es 1, llamamos a la función para agregar un nuevo dato
            agregar()
        elif opcion == "2":  # Si la opción es 2, llamamos a la función para eliminar un dato por su ID
            eliminar()
        elif opcion == "3":  # Si la opción es 3, llamamos a la función para agregar en una posicion específica
            agregar_en_posicion()
        elif opcion == "4":  # Si la opción es '4', llamamos a la función para mostrar los datos almacenados
            mostrar_datos()
        elif opcion == "terminar":  # Si escribe 'terminar', salimos
            print("\n")
            print("¡Hasta luego, Rey 👑! ¡Fiera 🦁! ¡Campeón 🏆! ¡Crack 🔥! ¡Máquina 🛠️! ¡Leyenda 🌟!  ¡Titán ⚡! ¡Fenómeno 🚀!") # Mensaje de despedida
            print("\n")
            break  # Rompemos el bucle y terminamos la ejecución del programa
        else:  # Si la opción no es válida, mostramos un mensaje de error
            print("\n")
            print("❌ Opción no válida. Intente de nuevo.")  # Mensaje indicando que la opción no es válida

#----------------------------------------------------------------------------------------------------------------------------------------------------------
menu() # Iniciamos el programa llamando a la función 'menu()'