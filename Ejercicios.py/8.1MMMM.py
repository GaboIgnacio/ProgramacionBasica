# Analizar tráfico TLS/SSL y extraer información de certificados.
import pyshark
import csv
interfaz_red = 'Wi-Fi'
filtro_display = 'ssl || tls'
captura = pyshark.LiveCapture(interface=interfaz_red, display_filter=filtro_display)
datos_certificados = []
print("Capturando tráfico TLS/SSL y extrayendo información de certificados...\n")
for paquete in captura.sniff_continuously(packet_count=20):
    try:
        if 'ssl' in paquete:
            ssl_layer = paquete.ssl
            try:
                server_name = ssl_layer.handshake_extensions_server_name
            except AttributeError:
                server_name = 'N/A'

            try:
                cert_valid_from = ssl_layer.handshake_cert_validity_not_before
            except AttributeError:
                cert_valid_from = 'N/A'

            try:
                cert_valid_to = ssl_layer.handshake_cert_validity_not_after
            except AttributeError:
                cert_valid_to = 'N/A'
            hora = paquete.sniff_time.strftime("%H:%M:%S")
            ip_origen = paquete.ip.src
            ip_destino = paquete.ip.dst
            print(f"[{hora}] {ip_origen} → {ip_destino} | Server Name: {server_name} | Validez: {cert_valid_from} - {cert_valid_to}")
            datos_certificados.append([hora, ip_origen, ip_destino, server_name, cert_valid_from, cert_valid_to])
    except AttributeError:
        continue
with open('certificados_tls.csv', mode='w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(['Hora', 'IP Origen', 'IP Destino', 'Server Name', 'Validez Desde', 'Validez Hasta'])
    escritor_csv.writerows(datos_certificados)
print("\nArchivo 'certificados_tls.csv' guardado con la información de certificados.")
