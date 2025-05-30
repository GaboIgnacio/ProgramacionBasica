# Medir el tiempo de respuesta de servidores DNS.
import pyshark
import csv

INTERFAZ = 'Wi-Fi'
ARCHIVO_CSV = 'tiempo_respuesta_dns.csv'

print("Iniciando captura de paquetes DNS...\n")
captura = pyshark.LiveCapture(interface=INTERFAZ, display_filter='dns')

consultas = {}  # clave: (id, ip_origen), valor: tiempo de consulta
resultados = []  # lista para guardar resultados: [IP cliente, IP servidor DNS, id consulta, tiempo_respuesta_ms]

for packet in captura.sniff_continuously(packet_count=30):
    try:
        hora = float(packet.sniff_timestamp)
        ip_origen = packet.ip.src
        ip_destino = packet.ip.dst
        dns_id = packet.dns.id
        
        # Aquí va el cambio para evitar el error
        flag_resp = packet.dns.flags_response
        # Convertimos a booleano según el valor del flag
        es_respuesta = flag_resp == 'True' or flag_resp == '1'
        
        if not es_respuesta:
            # Guardamos hora de consulta, usando id y IP origen para identificarla
            consultas[(dns_id, ip_origen)] = hora
        else:
            # Es respuesta, buscamos consulta previa
            clave = (dns_id, ip_destino)  # La respuesta tiene IP origen que fue destino en la consulta
            if clave in consultas:
                tiempo_consulta = consultas[clave]
                latencia = (hora - tiempo_consulta) * 1000 
                resultados.append([ip_origen, ip_destino, dns_id, round(latencia, 2)])
                print(f"Cliente: {ip_origen} -> Servidor DNS: {ip_destino} | Consulta ID: {dns_id} | Tiempo de respuesta: {round(latencia, 2)} ms")
                # Eliminamos para evitar que se acumule memoria
                del consultas[clave]
    except AttributeError:
        continue

with open(ARCHIVO_CSV, mode='w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['IP Cliente', 'IP Servidor DNS', 'ID Consulta', 'Tiempo de Respuesta (ms)'])
    escritor.writerows(resultados)

print(f"\nDatos guardados en '{ARCHIVO_CSV}'.")

# Sin round(): latencia exacta, pero con muchos decimales.
# Con round(latencia, 2): latencia con solo 2 decimales, más legible y práctica.


