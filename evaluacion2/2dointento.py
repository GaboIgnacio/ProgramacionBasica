 # Alumno: Gabriel Melo
# Sección: Informática y Ciberseguridad - Instituto Profesional Los Leones

import re

# Lista que contiene los registros de firewall
datos = [
    ["192.168.1.10", "AB:CD:EF:12:34:56", "172.16.0.5", 443, "TCP", "Permitido"],
    ["10.0.0.1", "A1-B2-C3-D4-E5-F6", "8.8.8.8", 53, "UDP", "Denegado"]
]

# ---------------- VALIDACIONES ----------------

# Validar IP con expresiones regulares y condiciones específicas
def validar_ip(mensaje):
    patron_ipv4 = re.compile(r'^([0-9]{1,3}\.){3}[0-9]{1,3}$')
    while True:
        ip = input(mensaje)
        if not patron_ipv4.match(ip):
            print("❌ IP inválida. Formato incorrecto.")
            continue
        octetos = ip.split(".")
        if int(octetos[3]) == 0:
            print("❌ El último octeto no puede ser 0.")
            continue
        if all(0 <= int(o) <= 255 for o in octetos):
            return ip
        else:
            print("❌ Algún octeto supera 255.")

# Validar MAC con expresiones regulares
def validar_mac():
    patron_mac = re.compile(r'^[0-9A-Fa-f]{2}([-:])[0-9A-Fa-f]{2}(\1[0-9A-Fa-f]{2}){4}$')
    while True:
        mac = input("Ingrese la MAC address (Ej: AB:CD:EF:12:34:56): ")
        if patron_mac.match(mac):
            return mac
        else:
            print("❌ MAC inválida.")

# Validar número de puerto
def validar_puerto():
    while True:
        try:
            puerto = int(input("Ingrese el puerto de destino (1-65535): "))
            if 1 <= puerto <= 65535:
                return puerto
            else:
                print("❌ Puerto fuera de rango.")
        except ValueError:
            print("❌ Ingrese un número válido.")

# Validar tipo de protocolo
def elegir_protocolo():
    opciones = ["TCP", "UDP", "ICMP", "ALL"]
    while True:
        protocolo = input("Protocolo (TCP/UDP/ICMP/ALL): ").upper()
        if protocolo in opciones:
            return protocolo
        else:
            print("❌ Opción inválida.")

# Validar si está permitido o denegado
def permitido_denegado():
    while True:
        estado = input("¿Permitido o Denegado?: ").lower()
        if estado in ["permitido", "denegado"]:
            return estado.capitalize()
        else:
            print("❌ Escriba 'Permitido' o 'Denegado'.")

# ---------------- FUNCIONES ----------------

# Agregar nuevo registro
def agregar_dato():
    print("\n--- Agregar nuevo registro ---")
    ip_origen = validar_ip("IP Origen: ")
    mac = validar_mac()
    ip_destino = validar_ip("IP Destino: ")
    puerto = validar_puerto()
    protocolo = elegir_protocolo()
    estado = permitido_denegado()
    datos.append([ip_origen, mac, ip_destino, puerto, protocolo, estado])
    print("✅ Registro agregado correctamente.")

# Eliminar registro por ID
def eliminar_dato():
    mostrar_datos()
    try:
        indice = int(input("Ingrese el ID a eliminar: "))
        if 0 <= indice < len(datos):
            datos.pop(indice)
            print("✅ Registro eliminado.")
        else:
            print("❌ ID fuera de rango.")
    except ValueError:
        print("❌ Ingrese un número válido.")

# Insertar registro en ubicación específica
def insertar_dato():
    try:
        indice = int(input("Ingrese la posición para insertar: "))
        if 0 <= indice <= len(datos):
            ip_origen = validar_ip("IP Origen: ")
            mac = validar_mac()
            ip_destino = validar_ip("IP Destino: ")
            puerto = validar_puerto()
            protocolo = elegir_protocolo()
            estado = permitido_denegado()
            datos.insert(indice, [ip_origen, mac, ip_destino, puerto, protocolo, estado])
            print("✅ Registro insertado.")
        else:
            print("❌ Posición inválida.")
    except ValueError:
        print("❌ Ingrese un número válido.")

# Mostrar todos los datos
def mostrar_datos():
    print("\n--- Registros del Firewall ---")
    print("ID | IP Origen       | MAC Address          | IP Destino      | Puerto | Protocolo | Estado")
    print("-" * 85)
    for i, d in enumerate(datos):
        print(f"{i:<2} | {d[0]:<15} | {d[1]:<20} | {d[2]:<15} | {d[3]:<6} | {d[4]:<8} | {d[5]}")
    print()

# ---------------- MENÚ ----------------

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar dato")
        print("2. Eliminar dato")
        print("3. Insertar dato en posición específica")
        print("4. Ver todos los datos")
        print("5. Salir (escribe 'terminar')")
        opcion = input("Ingrese una opción: ").lower()

        if opcion == "1":
            agregar_dato()
        elif opcion == "2":
            eliminar_dato()
        elif opcion == "3":
            insertar_dato()
        elif opcion == "4":
            mostrar_datos()
        elif opcion == "5" or opcion == "terminar":
            print("👋 Programa finalizado.")
            break
        else:
            print("❌ Opción inválida.")

# ---------------- EJECUCIÓN ----------------

menu()
