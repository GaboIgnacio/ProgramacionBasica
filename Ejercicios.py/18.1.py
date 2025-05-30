# Analizar el tamaño promedio de paquetes en una captura de red.
import pyshark
import csv
INTERFAZ = 'Wi-Fi'
ARCHIVO_CSV = 'tamanios_paquetes.csv'
NUM_PAQUETES = 10
print("Iniciando captura para análisis de tamaño de paquetes...\n")
captura = pyshark.LiveCapture(interface=INTERFAZ)
datos_paquetes = []
total_bytes = 0
contador = 0
for packet in captura.sniff_continuously(packet_count=NUM_PAQUETES):
    try:
        tamaño = int(packet.length)
        total_bytes += tamaño
        contador += 1
        datos_paquetes.append([contador, tamaño])
        print(f"Paquete #{contador} - Tamaño: {tamaño} bytes")
    except AttributeError:
        continue
promedio = total_bytes / contador if contador > 0 else 0
with open(ARCHIVO_CSV, mode='w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(['Número de Paquete', 'Tamaño (bytes)'])
    writer.writerows(datos_paquetes)
    writer.writerow([])
    writer.writerow(['Promedio', promedio])
print(f"\nTamaño promedio de paquetes: {promedio:.2f} bytes")
print(f"Datos guardados en '{ARCHIVO_CSV}'.")
