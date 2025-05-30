# Filtrar paquetes UDP y analizar patrones de comunicación, guardado CSV al final.
import pyshark
import csv
interfaz = 'Wi-Fi'  
filtro = 'udp'
captura = pyshark.LiveCapture(interface=interfaz, display_filter=filtro)
conteo_udp = {}
datos_udp = []
print("Escuchando paquetes UDP...\n")
for paquete in captura.sniff_continuously(packet_count=20):
    try:
        ip_origen = paquete.ip.src
        ip_destino = paquete.ip.dst
        puerto_origen = paquete.udp.srcport
        puerto_destino = paquete.udp.dstport
        hora = paquete.sniff_time.strftime("%H:%M:%S")
        print(f"[{hora}] {ip_origen}:{puerto_origen} → {ip_destino}:{puerto_destino}")
        datos_udp.append([hora, ip_origen, puerto_origen, ip_destino, puerto_destino])
        if ip_origen in conteo_udp:
            conteo_udp[ip_origen] += 1
        else:
            conteo_udp[ip_origen] = 1
    except AttributeError:
        continue 
with open('trafico_udp.csv', mode='w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['Hora', 'IP Origen', 'Puerto Origen', 'IP Destino', 'Puerto Destino'])
    escritor.writerows(datos_udp)
print("\n📊 Resumen de comunicación UDP:")
for par, cantidad in conteo_udp.items():
    print(f" - {par}: {cantidad} paquetes")
