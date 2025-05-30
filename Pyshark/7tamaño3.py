import pyshark
import csv
INTERFAZ = 'Wi-Fi'
cap = pyshark.LiveCapture(interface=INTERFAZ)
paquetes_web = []
print("Capturando 500 paquetes...\n")
for packet in cap.sniff_continuously(packet_count=500):
    try:
        if hasattr(packet, 'ip'):
            origen = packet.ip.src
            destino = packet.ip.dst
            protocolo = packet.highest_layer
            tiempo = packet.sniff_time
            tamaño = int(packet.length)

            if protocolo == "DNS" and hasattr(packet.dns, 'qry_name'):
                dominio = packet.dns.qry_name
                print(f"DNS → Dominio consultado: {dominio} (por {origen})")
                paquetes_web.append([tiempo, origen, destino, protocolo, dominio])
            elif protocolo in ["HTTP", "HTTPS"]:
                print(f"Tráfico Web → Origen: {origen} → Destino: {destino} ({protocolo})")
                paquetes_web.append([tiempo, origen, destino, protocolo, ""])
            elif tamaño > 1000:
                print(f"Paquete grande (1000+ bytes) → {tamaño} bytes | Origen: {origen} → Destino: {destino}")
    except AttributeError:
        continue
print(f"\nTotal capturado para guardar: {len(paquetes_web)} entradas.")
# Guardar CSV si hay datos
if paquetes_web:
    with open("trafico_web_dns.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Tiempo", "IP Origen", "IP Destino", "Protocolo", "Dominio"])
        writer.writerows(paquetes_web)
    print("✅ Datos guardados en 'trafico_web_dns.csv'.")
else:
    print("⚠️ No se capturó tráfico relevante, no se guardó el archivo.")
