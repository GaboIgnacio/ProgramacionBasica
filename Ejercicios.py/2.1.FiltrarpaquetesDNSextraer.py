# Filtrar paquetes DNS y extraer los dominios consultados con guardado CSV.

import pyshark
import csv
INTERFAZ = 'Wi-Fi'  
ARCHIVO_CSV = 'dns_consultas.csv'
CONSULTAS_DNS = []
print("Capturando consultas DNS...\n")
captura = pyshark.LiveCapture(interface=INTERFAZ, display_filter='dns')
for paquete in captura.sniff_continuously(packet_count=10):
    try:
        hora = paquete.sniff_time
        dominio = paquete.dns.qry_name
        CONSULTAS_DNS.append([hora, dominio])
        print(f"{hora} - Dominio: {dominio}")
    except AttributeError:
        continue 

with open(ARCHIVO_CSV, mode='w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(['Hora', 'Dominio Consultado'])
    writer.writerows(CONSULTAS_DNS)
print(f"\nCaptura finalizada. Datos guardados en '{ARCHIVO_CSV}'")
