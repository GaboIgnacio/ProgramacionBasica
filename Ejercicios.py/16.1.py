# Calcular la latencia en conexiones TCP mediante análisis de SYN-ACK.

import pyshark
import csv
INTERFAZ = 'Wi-Fi'
ARCHIVO_CSV = 'latencia_tcp.csv'
print("Capturando paquetes TCP para calcular latencia (SYN -> SYN-ACK)...\n")
captura = pyshark.LiveCapture(interface=INTERFAZ, display_filter='tcp')
lista_syn = []
lista_latencias = []
for packet in captura.sniff_continuously(packet_count=50):  
    try:
        hora = float(packet.sniff_timestamp)
        ip_origen = packet.ip.src
        ip_destino = packet.ip.dst
        puerto_origen = packet.tcp.srcport
        puerto_destino = packet.tcp.dstport
        flags = packet.tcp.flags
        if flags == '0x0002': # Si el paquete es un SYN (inicio de conexión), lo guardamos
            lista_syn.append([ip_origen, ip_destino, puerto_destino, hora])
        elif flags == '0x0012': # Si el paquete es un SYN-ACK (respuesta del servidor al SYN)
            # Buscamos si ya habíamos guardado un SYN correspondiente
            for syn in lista_syn:
                # Verificamos que la IP destino del SYN sea ahora la IP origen del SYN-ACK
                # y que el puerto coincida (inversión del sentido de la conexión)
                if syn[0] == ip_destino and syn[1] == ip_origen and syn[2] == puerto_origen:
                    # Calculamos la latencia: diferencia de tiempo entre el SYN y el SYN-ACK
                    latencia = (hora - syn[3]) * 1000  # Pasamos a milisegundos
                    print(f"Cliente: {syn[0]} -> Servidor: {syn[1]} | Puerto: {syn[2]} | Latencia: {round(latencia, 2)} ms")

                    lista_latencias.append([syn[0], syn[1], syn[2], round(latencia, 2)])

                    lista_syn.remove(syn) # Quitamos el SYN usado de la lista para evitar duplicados
                    break 
    except AttributeError:
        continue
with open(ARCHIVO_CSV, mode='w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(['IP Cliente', 'IP Servidor', 'Puerto Destino', 'Latencia (ms)'])
    writer.writerows(lista_latencias)
print(f"\nLatencias guardadas en '{ARCHIVO_CSV}'.")
