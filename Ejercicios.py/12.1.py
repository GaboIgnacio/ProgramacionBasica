# Reconstruir sesiones TCP y analizar flujos de datos.
import pyshark
import csv
INTERFAZ = 'Wi-Fi'
ARCHIVO_CSV = 'sesiones_tcp.csv'
sesiones_tcp = {}
print("Iniciando captura de sesiones TCP...\n")
captura = pyshark.LiveCapture(interface=INTERFAZ, display_filter='tcp')
for packet in captura.sniff_continuously(packet_count=50):
    try:
        ip_origen = packet.ip.src
        ip_destino = packet.ip.dst
        puerto_origen = packet.tcp.srcport
        puerto_destino = packet.tcp.dstport
        hora = packet.sniff_time
        longitud = packet.length
        flags = packet.tcp.flags
        clave_sesion = f"{ip_origen}:{puerto_origen} -> {ip_destino}:{puerto_destino}"
        if clave_sesion not in sesiones_tcp:
            sesiones_tcp[clave_sesion] = []
        sesiones_tcp[clave_sesion].append([hora, ip_origen, puerto_origen, ip_destino, puerto_destino, longitud, flags])
        print(f"Sesión: {clave_sesion}, Hora: {hora}, Longitud: {longitud}, Flags TCP: {flags}")
    except AttributeError:
        continue
print("\nResumen de sesiones TCP capturadas:")
for stream_id, paquetes in sesiones_tcp.items():
    print(f"\n=== Sesión TCP: {stream_id} ===")
    for p in paquetes:
        print(p)
with open(ARCHIVO_CSV, mode='w', newline='', encoding='utf-8') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(['Sesión', 'Hora', 'IP Origen', 'Puerto Origen', 'IP Destino', 'Puerto Destino', 'Longitud', 'Flags TCP'])
    for stream_id, paquetes in sesiones_tcp.items():
        for p in paquetes:
            writer.writerow([stream_id] + p)
print(f"\n✅ Los datos han sido guardados correctamente en '{ARCHIVO_CSV}'.")

