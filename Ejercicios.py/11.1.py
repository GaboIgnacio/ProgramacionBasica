# Extraer archivos transmitidos en tráfico HTTP.
import pyshark
import csv
archivos_http = []
captura = pyshark.LiveCapture(interface='Wi-Fi', display_filter='http')
print("Capturando paquetes HTTP...")
for paquete in captura.sniff_continuously(packet_count=20):
    try:
        if hasattr(paquete.http, 'content_disposition'):
            content_disp = paquete.http.content_disposition.lower()
            if 'filename=' in content_disp:
                nombre_archivo = content_disp.split('filename=')[1].strip('"')
                hora = paquete.sniff_time.strftime("%H:%M:%S")
                archivos_http.append([hora, nombre_archivo])
                print(f"[{hora}] Archivo detectado: {nombre_archivo}")
    except AttributeError:
        continue
with open('archivos_http.csv', mode='w', newline='', encoding='utf-8') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(['Hora', 'Nombre Archivo'])
    escritor.writerows(archivos_http)

print("\nArchivo 'archivos_http.csv' guardado con la info de archivos HTTP detectados.")
