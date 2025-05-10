# Alumna: Teresita Cañete
# Sección: Ingeniería en Ciberseguridad A


### Funcion validar ip ######
def validar_ip(ip):
    lista = ip.split(".") # separa la ip con split donde esta el punto, osea en 4 parte y crea una lista de string

    if len(lista) != 4: # si la longitud de la lista es distinta a 4 retorna flase
        return False

    for i in range(4): # recorre la lista
        if not lista[i].isdigit(): # revisa si los elementos de la lista son digitos
            return False
        numero = int(lista[i])  #  como split los tranforma en string aca los volvemos int para poder hacer operaciones
        if numero < 0 or numero > 255: #  si numero es menor a 0 mayor a 255 retorna false
            return False
        if i == 3 and numero == 0:  # valida que ultimo octeto no puede ser 0
            return False
    return True # si pasa esas validaciones retorna true


###### Función validar mac ######
def validar_mac(mac):
    lista = mac.split(":") # separa la mac ":" crea una lista
    if len(lista) != 6: # lo mismo que arriba valida que si la lista conseguida es distinta a 6 retorna false
        return False
    for e in lista: # recorre la lista
        if len(e) != 2: # si cada elemento de la lista de longitud es distinto a 2 retorna falso
            return False
        for c in e: # luego este for recorre los caracteres dentro de cada elemento de la lista
            if not c.lower() in "0123456789abcdef": # cada caracter lo convierte a minuscula y si no esta dentro de los caracteres hexadecimales es false
                return False
    return True # si pasa esas validaciones retorna true

######  Función puertos ######
def validar_puerto(puerto):
    if not puerto.isdigit():  #  valida que sean digitos
        return False
    puertoE = int(puerto)  #  convierte a enteros
    if puertoE < 1 or puertoE > 65535:  # Verifica rango válido de puertos (1 a 65535)
        return False

    return True

####### Validar protocolo válido  ########
def validar_protocolo(protocolo):
    protocolos_validos = ["tcp", "udp", "icmp", "all"] # lista de protocolos validos
    return protocolo.lower() in protocolos_validos # pasa protocolos a minusculas y verifica que esten en la lista

####### Función permitido o denegado #######
def validar_permisos(permiso):
    return permiso.lower() in ["permitido", "denegado"]


#### Inicio del CRUD #####
######   Función agregar registros  ######
def agregar_registro(lista):
    ip_origen = input("Ingresa IP de origen: ") # input para agregar ip
    while not validar_ip(ip_origen): # inicio de ciclo, llamo a la función que valida la ip y paso como parametro ip obtenida,
        print("❌ IP inválida.") # si no pasa la validación
        ip_origen = input("Ingresa IP de origen nuevamente: ") # pedir que ingrese nuevamente

    mac = input("Ingresa dirección MAC: ") # input para agregar mac
    while not validar_mac(mac): # ciclo y llamar a funcion que valida la mac, pasar parametro obtenido del input
        print("❌ MAC inválida.") # mensaje de error
        mac = input("Ingresa MAC nuevamente: ") # pedir nuevo ingreso

    ip_destino = input("Ingresa IP de destino: ") # input para agregar ip destino
    while not validar_ip(ip_destino): # ciclo y llamar a funcion que valida ip, pasar parametro(ip obtenida en input)
        print("❌ IP inválida.") # mensaje de error
        ip_destino = input("Ingresa IP de destino nuevamente: ") # pedir nuevo ingreso

    puerto = input("Ingresa puerto: ") # input para agregar puerto
    while not validar_puerto(puerto): # ciclo y llamar a función que valida puerto, pasar valor obtenido en input
        print("❌ Puerto inválido.") # mensaje error
        puerto = input("Ingresa puerto nuevamente: ") # pedir nuevo igreso
    puerto = int(puerto)  # Lo convertimos a número para guardarlo

    protocolo = input("Protocolo (TCP, UDP, ICMP, ALL): ") # input para agregar protocolo
    while not validar_protocolo(protocolo): # ciclo y llamar a función pasar protocolo como parámetro
        print("❌ Protocolo inválido.") # mensaje error
        protocolo = input("Protocolo nuevamente: ") # pedir nuevo igreso
    protocolo = protocolo.upper() # convertir en mayúsculas

    permiso = input("¿Permitido o denegado?: ") # input para agregar permisos
    while not validar_permisos(permiso): # función agregar permisos, solo permitio o denegado
        print("❌ Valor inválido.") # mensaje error
        permiso = input("Escribe 'permitido' o 'denegado': ") # ingresar solo permitido o denegado
    permiso = permiso.lower() # pasar a minuscola

    nuevo = [ip_origen, mac, ip_destino, puerto, protocolo, permiso] # nuevo ingreso
    lista.append(nuevo) # Agregar a lista
    print("✅ Registro agregado con éxito.") # mensaje de éxito

####### Función ver datos ######
def ver_datos(lista):
    if not lista: # si no está en la lista
        print("📭 No hay registros para mostrar.") # mensaje
        return

    print("\n📋 Lista de registros:") # si hay datos mensaje
    for i in range(len(lista)): # for para recorrer la lista e imprimir datos
        registro = lista[i]
        print(f"ID: {i} | IP Origen: {registro[0]} | MAC: {registro[1]} | IP Destino: {registro[2]} | Puerto: {registro[3]} | Protocolo: {registro[4]} | Permiso: {registro[5]}")

###### Función eliminar ######
def eliminar_registro(lista):
    if not lista:
        print("📭 No hay registros para eliminar.") # si no hay datos no muestras
        return

    ver_datos(lista)  # Mostrar los registros actuales

    id_str = input("Ingresa el ID del registro que deseas eliminar: ") # input para agregar el ID del elemento que quiere eliminar
    while not id_str.isdigit() or int(id_str) < 0 or int(id_str) >= len(lista): # Valida que el ID ingresado sea un número entero positivo y que este dentro de la lista
        print("❌ ID inválido.") # mensaje de error
        id_str = input("Ingresa un ID válido: ") # pedir nuevo ingreso

    id_eliminar = int(id_str) # convertir id a entero para poder usarlo como índice
    registro = lista[id_eliminar] # Obtiene el registro al ID para mostrarlo antes de eliminar

    # Confirmación antes de eliminar
    print(f"\n🗑️ Registro seleccionado: {registro}")
    confirmar = input("¿Estás seguro que deseas eliminar este registro? (s/n): ")

    if confirmar.lower() != "s":
        print("❌ Eliminación cancelada.")
        return

    eliminado = lista.pop(id_eliminar)  # Elimina el registro
    print(f"✅ Registro eliminado: {eliminado}") # mensaje exitoso

####### Función para agregar en lugar definido ########
def agregar_en_posicion(lista):
    if not lista:
        print("⚠️ Lista vacía.")# no hay datos

    else:
        ver_datos(lista) # si hay datos

    # Pedir posición
    posicion_str = input(f"Ingrese la posición para insertar (0 a {len(lista)}): ")
    while not posicion_str.isdigit() or int(posicion_str) < 0 or int(posicion_str) > len(lista): # valida que ingreso sea numero entero y que este dentro de rago de lista
        print("❌ Posición inválida.")
        posicion_str = input(f"Ingresa una posición válida (0 a {len(lista)}): ")
    posicion = int(posicion_str) # convierte en entero

    # Pedir y validar datos igual que en agregar_registro()
    ip_origen = input("Ingresa IP de origen: ")
    while not validar_ip(ip_origen):
        print("❌ IP inválida.")
        ip_origen = input("Ingresa IP de origen nuevamente: ")

    mac = input("Ingresa dirección MAC: ")
    while not validar_mac(mac):
        print("❌ MAC inválida.")
        mac = input("Ingresa MAC nuevamente: ")

    ip_destino = input("Ingresa IP de destino: ")
    while not validar_ip(ip_destino):
        print("❌ IP inválida.")
        ip_destino = input("Ingresa IP de destino nuevamente: ")

    puerto = input("Ingresa puerto: ")
    while not validar_puerto(puerto):
        print("❌ Puerto inválido.")
        puerto = input("Ingresa puerto nuevamente: ")
    puerto = int(puerto)

    protocolo = input("Protocolo (TCP, UDP, ICMP, ALL): ")
    while not validar_protocolo(protocolo):
        print("❌ Protocolo inválido.")
        protocolo = input("Protocolo nuevamente: ")
    protocolo = protocolo.upper()

    permiso = input("¿Permitido o denegado?: ")
    while not validar_permisos(permiso):
        print("❌ Valor inválido.")
        permiso = input("Escribe 'permitido' o 'denegado': ")
    permiso = permiso.lower()

    nuevo = [ip_origen, mac, ip_destino, puerto, protocolo, permiso]
    lista.insert(posicion, nuevo)

    print(f"✅ Registro insertado en la posición {posicion}.")





#Lista precargadas
lista_principal = [
    ["192.168.1.1", "AA:BB:CC:DD:EE:FF", "8.8.8.8", 80, "TCP", "permitido"],
    ["10.0.0.2", "11:22:33:44:55:66", "1.1.1.1", 443, "UDP", "denegado"]
]
###########   Menú  ###################
def mostrar_menu():
    print("\n===== Menú Bienvenido =====")
    print("1. Agregar nuevo registro")
    print("2. Eliminar registro por ID")
    print("3. Agregar registro en ubicación específica")
    print("4. Ver todos los datos")
    print("Escribe 'terminar' para salir")

###### bucle para las opciones llamado la funciones creadas arriba ######
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion.lower() == "terminar":
        print("👋 Saliendo del sistema...")
        break
    elif opcion == "1":
        agregar_registro(lista_principal)
    elif opcion == "2":
        eliminar_registro(lista_principal)
    elif opcion == "3":
        agregar_en_posicion(lista_principal)
        pass
    elif opcion == "4":
        ver_datos(lista_principal)
    else:
        print("❌ Opción no válida. Intenta nuevamente.")


################## Fín ########################