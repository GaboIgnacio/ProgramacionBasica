# Identificar retransmisiones TCP y evaluar estabilidad de conexión.

import pyshark
import csv
INTERFAZ = 'Wi-Fi'
ARCHIVO_CSV = 'retransmisiones_tcp.csv'
NUM_PAQUETES = 50
print("Iniciando captura para identificar retransmisiones TCP...\n")
captura = pyshark.LiveCapture(interface=INTERFAZ, display_filter='tcp')
# Guardamos secuencias vistas por conexión: {(ip_src, ip_dst, port_src, port_dst): set(seq_nums)}
secuencias_vistas = {}
retransmisiones = []
contador_total = 0
contador_retransmisiones = 0
for packet in captura.sniff_continuously(packet_count=NUM_PAQUETES):
    try:
        ip_src = packet.ip.src
        ip_dst = packet.ip.dst
        port_src = packet.tcp.srcport
        port_dst = packet.tcp.dstport
        seq = int(packet.tcp.seq)
        clave = (ip_src, ip_dst, port_src, port_dst)
        if clave not in secuencias_vistas:
            secuencias_vistas[clave] = set()
        contador_total += 1
        if seq in secuencias_vistas[clave]:
            contador_retransmisiones += 1
            retransmisiones.append([ip_src, ip_dst, port_src, port_dst, seq])
            print(f"Retransmisión detectada: {ip_src}:{port_src} -> {ip_dst}:{port_dst} | Seq: {seq}")
        else:
            secuencias_vistas[clave].add(seq)
    except AttributeError:
        continue
with open(ARCHIVO_CSV, mode='w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(['IP Origen', 'IP Destino', 'Puerto Origen', 'Puerto Destino', 'Número de Secuencia'])
    writer.writerows(retransmisiones)
if contador_total > 0:
    tasa_retransmision = (contador_retransmisiones / contador_total) * 100
else:
    tasa_retransmision = 0
print(f"\nTotal paquetes TCP analizados: {contador_total}")
print(f"Retransmisiones detectadas: {contador_retransmisiones}")
print(f"Tasa de retransmisión: {tasa_retransmision:.2f}%")
print(f"Datos guardados en '{ARCHIVO_CSV}'.")
