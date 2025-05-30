# Detectar intentos de escaneo de puertos mediante análisis de paquetes TCP (guardado CSV al final).

import pyshark
import csv
interfaz_red = 'Wi-Fi'
filtro_display = 'tcp'
captura = pyshark.LiveCapture(interface=interfaz_red, display_filter=filtro_display)
escaneos_por_ip = {}
datos_escaneo = []
print("Detectando posibles escaneos de puertos...\n")
for paquete in captura.sniff_continuously(packet_count=50):
    try:
        ip_origen = paquete.ip.src
        puerto_destino = paquete.tcp.dstport
        hora = paquete.sniff_time.strftime("%H:%M:%S")
        datos_escaneo.append([hora, ip_origen, puerto_destino])
        if ip_origen in escaneos_por_ip:
            if puerto_destino not in escaneos_por_ip[ip_origen]:
                escaneos_por_ip[ip_origen].append(puerto_destino)
        else:
            escaneos_por_ip[ip_origen] = [puerto_destino]
        print(f"[{hora}] {ip_origen} → Puerto: {puerto_destino}")
    except AttributeError:
        continue
with open('escaneo_puertos.csv', mode='w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(['Hora', 'IP Origen', 'Puerto Destino'])
    escritor_csv.writerows(datos_escaneo)
print("\nResumen de IPs con múltiples intentos a distintos puertos:")
for ip, puertos in escaneos_por_ip.items():
    if len(puertos) >= 5:  # Umbral para sospechar escaneo
        print(f"{ip} intentó acceder a {len(puertos)} puertos: {puertos}")
    else:
        print(f"{ip} con {len(puertos)} intentos")
