# Nombre: Gabriel Melo
# Sección: 1 (Ingeniería en Ciberseguridad - Instituto Profesional Los Leones)

# Importamos re para validar MAC
import re

# Datos pre-cargados
datos = [
    ["192.168.1.2", "AA:BB:CC:DD:EE:FF", "10.0.0.2", 80, "TCP", "Permitido"],
    ["172.167.168.244", "24:01:20:02:20:25", "192.168.0.2", 443, "UDP", "Denegado"]
]

# Función para validar dirección IP
def validar_ip(mensaje):
    while True:
        ip = input(mensaje)
        octetos = ip.strip().split(".")
        if len(octetos) == 4 and all(o.isdigit() for o in octetos):
            octetos = list(map(int, octetos))
            if 1 <= octetos[0] <= 255 and all(0 <= o <= 255 for o in octetos[1:3]) and octetos[3] != 0:
                return ip
        print("❌ IP inválida. Recuerda: los primeros 3 octetos deben ser entre 0 y 255, y el último NO puede ser 0.")

# Función para validar MAC address
def validar_mac():
    while True:
        mac = input("Ingrese MAC (formato AA:BB:CC:DD:EE:FF): ").upper()
        if re.match("^([0-9A-F]{2}:){5}[0-9A-F]{2}$", mac):
            return mac
        print("❌ MAC inválida.")

# Función para validar puerto
def validar_puerto():
    while True:
        puerto = input("Ingrese Puerto (1-65535): ")
        if puerto.isdigit():
            puerto = int(puerto)
            if 1 <= puerto <= 65535:
                return puerto
        print("❌ Puerto inválido.")

# Función para elegir tipo de protocolo
def elegir_protocolo():
    opciones = ["TCP", "UDP", "ICMP", "ALL"]
    while True:
        proto = input("Ingrese protocolo (TCP/UDP/ICMP/ALL): ").upper()
        if proto in opciones:
            return proto
        print("❌ Opción inválida.")

# Función para elegir si se permite o no
def permitido_denegado():
    opciones = ["PERMITIDO", "DENEGADO"]
    while True:
        valor = input("¿Permitido o Denegado?: ").upper()
        if valor in opciones:
            return valor.capitalize()
        print("❌ Opción inválida.")

# Función para mostrar los datos
def mostrar_datos():
    print("\nDatos almacenados:")
    print("=" * 100)
    print(f"{'ID':<3}| {'IP Origen':<17} | {'MAC':<19} | {'IP Destino':<17} | {'Puerto':<7} | {'Protocolo':<9} | {'Estado'}")
    print("=" * 100)
    for i, d in enumerate(datos):
        print(f"{i:<3}| {d[0]:<17} | {d[1]:<19} | {d[2]:<17} | {str(d[3]):<7} | {d[4]:<9} | {d[5]}")
    print("=" * 100)

# Función para agregar datos
def agregar():
    print("Agregando nuevo registro:")
    ip_origen = validar_ip("Ingrese IP de Origen: ")
    mac = validar_mac()
    ip_destino = validar_ip("Ingrese IP de Destino: ")
    puerto = validar_puerto()
    protocolo = elegir_protocolo()
    estado = permitido_denegado()
    datos.append([ip_origen, mac, ip_destino, puerto, protocolo, estado])
    print("✅ Registro agregado exitosamente.")

# Función para eliminar dato por ID
def eliminar():
    mostrar_datos()
    while True:
        id_eliminar = input("Ingrese ID del dato a eliminar: ")
        if id_eliminar.isdigit():
            id_eliminar = int(id_eliminar)
            if 0 <= id_eliminar < len(datos):
                datos.pop(id_eliminar)
                print("✅ Dato eliminado correctamente.")
                break
            else:
                print("❌ ID fuera de rango.")
        else:
            print("❌ ID inválido.")

# Función para agregar en posición específica
def agregar_en_posicion():
    mostrar_datos()
    while True:
        id_insertar = input("Ingrese posición donde desea insertar: ")
        if id_insertar.isdigit():
            id_insertar = int(id_insertar)
            if 0 <= id_insertar <= len(datos):
                ip_origen = validar_ip("Ingrese IP de Origen: ")
                mac = validar_mac()
                ip_destino = validar_ip("Ingrese IP de Destino: ")
                puerto = validar_puerto()
                protocolo = elegir_protocolo()
                estado = permitido_denegado()
                datos.insert(id_insertar, [ip_origen, mac, ip_destino, puerto, protocolo, estado])
                print("✅ Dato insertado correctamente.")
                break
            else:
                print("❌ Posición fuera de rango.")
        else:
            print("❌ Posición inválida.")

# Función principal con menú
def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar nuevo dato")
        print("2. Eliminar dato por ID")
        print("3. Agregar en ubicación específica")
        print("4. Ver datos ingresados")
        print("5. Salir")
        opcion = input("Seleccione una opción: ").lower()

        if opcion == "1":
            agregar()
        elif opcion == "2":
            eliminar()
        elif opcion == "3":
            agregar_en_posicion()
        elif opcion == "4":
            mostrar_datos()
        elif opcion == "5" or opcion == "terminar":
            print("👋 Programa finalizado.")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")

# Iniciamos el programa
menu()
