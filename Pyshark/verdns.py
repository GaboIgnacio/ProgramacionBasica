import pyshark
import csv
INTERFAZ = 'Ethernet'  
PAQUETES_A_CAPTURAR = 20
ARCHIVO_SALIDA = "GabrielMelo.csv"

paquetes_web = []

print(f"📡 Toy capturando {PAQUETES_A_CAPTURAR} paquetes en '{INTERFAZ}' oe...\n")

captura = pyshark.LiveCapture(interface=INTERFAZ)

for paquete in captura.sniff_continuously(packet_count=PAQUETES_A_CAPTURAR):
    try:
        if not hasattr(paquete, 'ip'):
            continue
        origen = paquete.ip.src
        destino = paquete.ip.dst
        protocolo = paquete.highest_layer
        tiempo = paquete.sniff_time
        tamaño = int(paquete.length)
        if protocolo == "DNS" and hasattr(paquete.dns, 'qry_name'):
            dominio = paquete.dns.qry_name
            print(f"🧠 DNS → Dominio consultado: {dominio} (por {origen})")
            paquetes_web.append([tiempo, origen, destino, protocolo, dominio])

        elif tamaño > 1000:
            print(f"📦 Tráfico grande → Origen: {origen} → Destino: {destino} → Tamaño: {tamaño} bytes")

        elif protocolo == "HTTP":
            print(f"🌍 HTTP → Origen: {origen} → Destino: {destino}")
            paquetes_web.append([tiempo, origen, destino, protocolo, ""])

    except AttributeError:
        continue
with open(ARCHIVO_SALIDA, "w", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Tiempo", "IP Origen", "IP Destino", "Protocolo", "Dominio"])
    escritor.writerows(paquetes_web)
print(f"\n✅ Archivo guardado como '{ARCHIVO_SALIDA}'.")