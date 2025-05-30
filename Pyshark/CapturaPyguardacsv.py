# Captura 20 paquetes de red en tiempo real desde la interfaz de red especificada (Wi-Fi),
# filtra tráfico DNS y HTTP, y guarda información relevante en un archivo CSV.
import pyshark
import csv
INTERFAZ = 'Wi-Fi'  # Asegúrate que esta sea tu interfaz activa
cap = pyshark.LiveCapture(interface=INTERFAZ)
paquetes_web = []
print("⏳ Capturando 200 paquetes...\n")
for packet in cap.sniff_continuously(packet_count=200):
    try:
        if hasattr(packet, 'ip'):
            origen = packet.ip.src
            destino = packet.ip.dst
            protocolo = packet.highest_layer
            tiempo = packet.sniff_time
            if protocolo == "DNS" and hasattr(packet.dns, 'qry_name'):
                dominio = packet.dns.qry_name
                print(f"🌐 DNS → Dominio consultado: {dominio} (por {origen})")
                paquetes_web.append([tiempo, origen, destino, protocolo, dominio])

            elif protocolo in ["HTTP"]:
                print(f"Tráfico Web → Origen: {origen} → Destino: {destino} ({protocolo})")
                paquetes_web.append([tiempo, origen, destino, protocolo, ""])
    except AttributeError:
        continue
with open("tráfico_web_dns.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Tiempo", "IP Origen", "IP Destino", "Protocolo", "Dominio"])
    writer.writerows(paquetes_web)

print("\n✅ Datos guardados en 'tráfico_web_dns.csv'.")