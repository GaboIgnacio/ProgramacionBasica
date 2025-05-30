import pyshark
import csv
interfaz = 'Ethernet'
PAQUETES_A_CAPTURAR = 100
salida = "GabrielMelo.csv"
paquetes_web = []
def traducir_flags_tcp(flags_hex):
    flags_bin = bin(int(flags_hex, 16))[2:].zfill(8)
    nombres_flags = ['FIN', 'SYN', 'RST', 'PSH', 'ACK', 'URG', 'ECE', 'CWR']
    flags_activos = [nombre for i, nombre in enumerate(nombres_flags) if flags_bin[::-1][i] == '1']
    return ','.join(flags_activos)
print(f"Toy capturando {PAQUETES_A_CAPTURAR} paquetes en '{interfaz}' oe...\n")
captura = pyshark.LiveCapture(interface=interfaz)
for paquete in captura.sniff_continuously(packet_count=PAQUETES_A_CAPTURAR):
    try:
        if not hasattr(paquete, 'ip'):
            continue
        origen = paquete.ip.src
        destino = paquete.ip.dst
        protocolo = paquete.highest_layer
        tiempo = paquete.sniff_time
        tamaño = int(paquete.length)
        flags_legibles = ""
        if hasattr(paquete, 'tcp') and hasattr(paquete.tcp, 'flags'):
            flags_hex = paquete.tcp.flags.replace("0x", "")
            flags_legibles = traducir_flags_tcp(flags_hex)
            print(f" Flags TCP: {flags_legibles} ({origen} → {destino})")
        if protocolo == "DNS" and hasattr(paquete.dns, 'qry_name'):
            dominio = paquete.dns.qry_name
            print(f" DNS → Dominio consultado: {dominio} (por {origen})")
            paquetes_web.append([tiempo, origen, destino, protocolo, dominio, flags_legibles])
        elif tamaño > 1000:
            print(f" GRAN tráfico → Origen: {origen} → Destino: {destino} | Tamaño: {tamaño} bytes")
        elif protocolo == "HTTP":
            print(f" HTTP → Origen: {origen} → Destino: {destino}")
            paquetes_web.append([tiempo, origen, destino, protocolo, "", flags_legibles])
    except AttributeError:
        continue
with open(salida, "w", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Tiempo", "IP Origen", "IP Destino", "Protocolo", "Dominio", "Flags TCP"])
    escritor.writerows(paquetes_web)
print(f"\n✅ Captura guardada como '{salida}'.")
