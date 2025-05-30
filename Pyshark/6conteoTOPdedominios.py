import pyshark
import csv
from collections import Counter
capture = pyshark.LiveCapture(interface='Wi-Fi')
paquetes_dns = []
contador = 0
max_paquetes = 100
print("Iniciando captura de paquetes DNS...\n")
for packet in capture.sniff_continuously():
    if contador >= max_paquetes:
        break
    try:
        if hasattr(packet, 'dns') and hasattr(packet.dns, 'qry_name'):
            dominio = packet.dns.qry_name
            print(f"[{contador+1}] Dominio consultado: {dominio}")
            paquetes_dns.append(dominio)
            contador += 1
    except AttributeError:
        continue
conteo_dominios = Counter(paquetes_dns)
top_5_repetidos = [item for item in conteo_dominios.most_common(5) if item[1] > 1]
print("\n Top 5 dominios DNS más repetidos:")
for dominio, cantidad in top_5_repetidos:
    print(f"{dominio}: {cantidad} veces")
with open("top_5_dominios_dns.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Dominio", "Cantidad"])
    for dominio, cantidad in top_5_repetidos:
        writer.writerow([dominio, cantidad])
print("\n Captura finalizada.")
print(f"Total de paquetes DNS capturados: {contador}")
print("Top 5 dominios repetidos guardados 'top_5_dominios_dns.csv'.")