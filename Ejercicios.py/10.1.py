# Identificar paquetes con direcciones MAC sospechosas en la red.
import pyshark
import csv
interfaz_red = 'Wi-Fi'
# Lista básica de MAC sospechosas conocidas 
mac_sospechosas = [
    "00:11:22:33:44:55",
    "de:ad:be:ef:00:01",  
    "ff:ff:ff:ff:ff:ff",  
    "00:50:56:c0:00:08",  
    "08:00:27:12:34:56",  
    "02:00:00:00:00:01",  
]
paquetes_sospechosos = []
captura = pyshark.LiveCapture(interface=interfaz_red)
print("Detectando paquetes con MAC sospechosas...\n")
for paquete in captura.sniff_continuously(packet_count=10):
    try:
        mac_origen = paquete.eth.src.lower() # Extraemos MAC origen y destino
        mac_destino = paquete.eth.dst.lower()
        hora = paquete.sniff_time.strftime("%H:%M:%S") # Hora en que se capturó el paquete
        # Verificamos si alguna MAC está en la lista de sospechosas
        if mac_origen in mac_sospechosas or mac_destino in mac_sospechosas:
            print(f"[{hora}] MAC sospechosa detectada: {mac_origen} → {mac_destino}")
            paquetes_sospechosos.append([hora, mac_origen, mac_destino])
    except AttributeError:
        continue
with open('mac_sospechosas.csv', mode='w', newline='', encoding='utf-8') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['Hora', 'MAC Origen', 'MAC Destino'])
    escritor.writerows(paquetes_sospechosos)
print("\nArchivo 'mac_sospechosas.csv' guardado con las detecciones.")
