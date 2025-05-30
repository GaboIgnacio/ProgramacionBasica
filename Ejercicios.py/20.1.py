# Detectar tráfico de streaming y analizar consumo de ancho de banda.
import pyshark
import csv
INTERFAZ = 'Wi-Fi'
ARCHIVO_CSV = 'consumo_streaming.csv'
print("Iniciando captura para análisis de tráfico streaming...\n")
# Ejemplo de filtro simple para RTSP (puerto 554) y HTTP/HTTPS (80 y 443)
captura = pyshark.LiveCapture(interface=INTERFAZ, display_filter='tcp.port == 554 or tcp.port == 80 or tcp.port == 443')
consumo_por_ip = {}
for packet in captura.sniff_continuously(packet_count=50):
    try:
        ip_origen = packet.ip.src
        ip_destino = packet.ip.dst
        length = int(packet.length) # tamaño total del paquete en bytes
        if ip_origen in consumo_por_ip:
            consumo_por_ip[ip_origen] += length
        else:
            consumo_por_ip[ip_origen] = length
        if ip_destino in consumo_por_ip:
            consumo_por_ip[ip_destino] += length
        else:
            consumo_por_ip[ip_destino] = length
    except AttributeError:
        continue
print("\nConsumo total de ancho de banda por IP (bytes):")
for ip, consumo in consumo_por_ip.items():
    print(f"{ip}: {consumo} bytes")
# Guardar en CSV
with open(ARCHIVO_CSV, mode='w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['IP', 'Consumo de Ancho de Banda (Bytes)'])
    for ip, consumo in consumo_por_ip.items():
        escritor.writerow([ip, consumo])
print(f"\nDatos guardados en '{ARCHIVO_CSV}'.")
