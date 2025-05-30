# Identificar patrones de comunicación en redes Wi-Fi.

import pyshark
import csv
INTERFAZ = 'Wi-Fi'
ARCHIVO_CSV = 'patrones_wifi.csv'
comunicaciones = {}
print("Iniciando captura de tráfico en Wi-Fi para identificar patrones...\n")
captura = pyshark.LiveCapture(interface=INTERFAZ)
for packet in captura.sniff_continuously(packet_count=50):
    try:
        if hasattr(packet, 'ip'):
            ip_origen = packet.ip.src
            ip_destino = packet.ip.dst
            protocolo = packet.transport_layer if hasattr(packet, 'transport_layer') else 'N/A'
            clave = (ip_origen, ip_destino, protocolo)
            if clave in comunicaciones:
                comunicaciones[clave] += 1
            else:
                comunicaciones[clave] = 1
            print(f"Paquete de {ip_origen} a {ip_destino} usando protocolo {protocolo}")
    except AttributeError:
        continue
print("\nPatrones detectados:")
with open(ARCHIVO_CSV, mode='w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(['IP Origen', 'IP Destino', 'Protocolo', 'Cantidad de Paquetes'])
    for clave, cantidad in comunicaciones.items():
        ip_origen, ip_destino, protocolo = clave
        print(f"{ip_origen} -> {ip_destino} | Protocolo: {protocolo} | Paquetes: {cantidad}")
        writer.writerow([ip_origen, ip_destino, protocolo, cantidad])
print(f"\nLos datos se guardaron en '{ARCHIVO_CSV}'.")
