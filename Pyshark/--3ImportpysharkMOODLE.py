import pyshark
INTERFAZ = 'Wi-Fi'
cap = pyshark.LiveCapture(interface=INTERFAZ)
paquetes_ip = []
for packet in cap.sniff_continuously(packet_count=10):
    if hasattr(packet, 'ip'):          
        origen = packet.ip.src
        destino = packet.ip.dst
        protocolo = packet.highest_layer
        paquetes_ip.append([packet.sniff_time, origen, destino, protocolo])
        print(f"Origen: {origen}, Destino: {destino}, Protocolo: {protocolo}")
print("\nLista de paquetes capturados:")
for paquete in paquetes_ip:
    print(paquete)
import csv
with open("captura_red.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Tiempo", "IP Origen", "IP Destino", "Protocolo"])
    writer.writerows(paquetes_ip)
print("Los datos han sido guardados en 'captura_red.csv'.")

