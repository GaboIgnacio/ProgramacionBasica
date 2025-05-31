import pyshark
import csv
INTERFAZ = 'Wi-Fi'
ARCHIVO_CSV = 'captura_icmp.csv'
paquetes_icmp = []
print("Iniciando captura de paquetes ICMP...\n")
captura = pyshark.LiveCapture(interface=INTERFAZ, display_filter='icmp')
for packet in captura.sniff_continuously(packet_count=10):
    try:
        hora = packet.sniff_time
        origen = packet.ip.src
        destino = packet.ip.dst
        tipo = packet.icmp.type
        codigo = packet.icmp.code
        paquetes_icmp.append([hora, origen, destino, tipo, codigo])
        print(f"Hora: {hora}, Origen: {origen}, Destino: {destino}, Tipo ICMP: {tipo}, Código: {codigo}")
    except AttributeError:
        continue  
print("\nLista de paquetes ICMP capturados:")
for paquete in paquetes_icmp:
    print(paquete)
with open(ARCHIVO_CSV, mode='w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(['Hora', 'IP Origen', 'IP Destino', 'Tipo ICMP', 'Código ICMP'])
    writer.writerows(paquetes_icmp)

print(f"\nLos datos han sido guardados en '{ARCHIVO_CSV}'.")


# Capturar tráfico en vivo y filtrar solo paquetes ICMP con guardado CSV.

# import pyshark
# import csv
# interfaz = 'Wi-Fi'
# archivo_csv = 'icmp_captura.csv'
# captura = pyshark.LiveCapture(interface=interfaz, display_filter='icmp')
# print("Capturando paquetes ICMP...\n")
# with open(archivo_csv, mode='w', newline='') as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(['Hora', 'IP Origen', 'IP Destino', 'Tipo ICMP', 'Código ICMP'])
#     for paquete in captura.sniff_continuously(packet_count=10):
#         try:
#             writer.writerow([
#                 paquete.sniff_time,
#                 paquete.ip.src,
#                 paquete.ip.dst,
#                 paquete.icmp.type,
#                 paquete.icmp.code
#             ])
#         except AttributeError:
#             continue
# print(f"\nCaptura finalizada. Paquetes ICMP guardados en '{archivo_csv}' ")