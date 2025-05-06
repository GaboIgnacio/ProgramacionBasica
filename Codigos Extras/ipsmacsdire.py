# Este código sirve para registrar múltiples paquetes de red ingresados por el usuario, 
# validando que las direcciones IP sean válidas en formato IPv4, las direcciones MAC estén bien escritas (con : o -), 
# y que los puertos de origen y destino sean números, para luego mostrar todos los datos organizados en una tabla clara
import re

# Validación de MAC
def es_mac_valida(dato):
    patron_mac = re.compile(r'^[0-9A-Fa-f]{2}([-:])[0-9A-Fa-f]{2}(\1[0-9A-Fa-f]{2}){4}$')
    return bool(patron_mac.match(dato))

# Validación de IPv4
def es_ipv4_valida(ip):
    patron_ipv4 = re.compile(r'^([0-9]{1,3}\.){3}[0-9]{1,3}$')
    if not patron_ipv4.match(ip):
        return False 
    octetos = ip.split('.')
    return all(octeto.isdigit() and 0 <= int(octeto) <= 255 for octeto in octetos)

# Listas para almacenar datos
ip_origen = []
ip_destino = []
puerto_origen = []
puerto_destino = []
macs = []

# Cantidad de paquetes
cantidad = int(input("Ingresa la cantidad de paquetes: "))

for i in range(cantidad):
    print(f"\nPaquete {i+1}:")

    ip_o = input("Ingresa la IP de Origen: ")
    while not es_ipv4_valida(ip_o):
        print("❌ IP de origen inválida. Intenta de nuevo.")
        ip_o = input("Ingresa la IP de Origen: ")
    ip_origen.append(ip_o)

    ip_d = input("Ingresa la IP de Destino: ")
    while not es_ipv4_valida(ip_d):
        print("❌ IP de destino inválida. Intenta de nuevo.")
        ip_d = input("Ingresa la IP de Destino: ")
    ip_destino.append(ip_d)

    p_o = input("Ingresa el Puerto de Origen: ")
    while not p_o.isdigit():
        print("❌ Puerto inválido. Solo se permiten números.")
        p_o = input("Ingresa el Puerto de Origen: ")
    puerto_origen.append(int(p_o))

    p_d = input("Ingresa el Puerto de Destino: ")
    while not p_d.isdigit():
        print("❌ Puerto inválido. Solo se permiten números.")
        p_d = input("Ingresa el Puerto de Destino: ")
    puerto_destino.append(int(p_d))

    mac = input("Ingresa la dirección MAC: ")
    while not es_mac_valida(mac):
        print("❌ Dirección MAC inválida. Intenta con formato válido (ej: AA:BB:CC:DD:EE:FF o AA-BB-CC-DD-EE-FF)")
        mac = input("Ingresa la dirección MAC: ")
    macs.append(mac)

# Mostrar resultados
print("="*80)
print(f"{'IP Origen':<15}{'IP Destino':<15}{'Puerto Origen':<15}{'Puerto Destino':<15}{'MAC'}")
print("-"*80)
for ip_o, ip_d, p_o, p_d, mac in zip(ip_origen, ip_destino, puerto_origen, puerto_destino, macs):
    print(f"{ip_o:<15}{ip_d:<15}{p_o:<15}{p_d:<15}{mac}")
print("="*80)
