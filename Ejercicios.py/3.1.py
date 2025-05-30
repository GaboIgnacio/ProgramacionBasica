# Detectar paquetes TCP con flags SYN y analizar intentos de conexión. con guardado Csv
import pyshark
import csv

INTERFAZ = 'Wi-Fi'
FILTRO_DISPLAY = 'tcp.flags.syn == 1 and tcp.flags.ack == 0'
ARCHIVO_CSV = 'intentos_syn.csv'
DATOS_SYN = []
intentos_por_ip = {}
print("Detectando intentos de conexión...\n")
captura = pyshark.LiveCapture(interface=INTERFAZ, display_filter=FILTRO_DISPLAY)
for paquete in captura.sniff_continuously(packet_count=10):
    try:
        ip_origen = paquete.ip.src
        ip_destino = paquete.ip.dst
        puerto_destino = paquete.tcp.dstport
        hora = paquete.sniff_time.strftime("%H:%M:%S")

        print(f"[{hora}] {ip_origen} → {ip_destino}:{puerto_destino}")
        DATOS_SYN.append([hora, ip_origen, ip_destino, puerto_destino])
        if ip_origen in intentos_por_ip:
            intentos_por_ip[ip_origen] += 1
        else:
            intentos_por_ip[ip_origen] = 1
    except AttributeError:
        continue
with open(ARCHIVO_CSV, mode='w', newline='') as archivo:
    escritor_csv = csv.writer(archivo)
    escritor_csv.writerow(['Hora', 'IP Origen', 'IP Destino', 'Puerto Destino'])
    escritor_csv.writerows(DATOS_SYN)
print("\nResumen de intentos de conexión:")
for ip, cantidad in intentos_por_ip.items():
    print(f" - {ip}: {cantidad} intentos")
print(f"\nDatos guardados en '{ARCHIVO_CSV}'")

