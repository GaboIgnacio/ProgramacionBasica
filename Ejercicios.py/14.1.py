# Analizar tráfico VoIP y extraer paquetes RTP.

import pyshark
import csv
INTERFAZ = 'Wi-Fi'
ARCHIVO_CSV = 'paquetes_rtp.csv'
paquetes_rtp = []
print("Iniciando captura de paquetes RTP...\n")
captura = pyshark.LiveCapture(interface=INTERFAZ, display_filter='rtp')

for packet in captura.sniff_continuously(packet_count=20):
    try:
        hora = packet.sniff_time
        if hasattr(packet, 'rtp'):
            secuencia = packet.rtp.seq
            timestamp = packet.rtp.timestamp
            if hasattr(packet, 'ip'):
                ip_origen = packet.ip.src
                ip_destino = packet.ip.dst
            else:
                ip_origen = 'N/A'
                ip_destino = 'N/A'
            paquetes_rtp.append([hora, ip_origen, ip_destino, secuencia, timestamp])
            print(f"Hora: {hora}, IP Origen: {ip_origen}, IP Destino: {ip_destino}, Secuencia RTP: {secuencia}, Timestamp: {timestamp}")
    except AttributeError:
        continue
print("\nLista de paquetes RTP capturados:")
for p in paquetes_rtp:
    print(p)

with open(ARCHIVO_CSV, mode='w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(['Hora', 'IP Origen', 'IP Destino', 'Secuencia RTP', 'Timestamp RTP'])
    writer.writerows(paquetes_rtp)

print(f"\nLos datos han sido guardados en '{ARCHIVO_CSV}'.")
