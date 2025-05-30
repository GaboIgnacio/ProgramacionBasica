# Identificar tráfico malicioso basado en firmas de malware con guardado CSV al final.
import pyshark
import csv
interfaz_red = 'Wi-Fi'
filtro_display = 'tcp or http'
firmas_malware = ["malicious_signature_1", "bad_payload_example", "eviluseragent", "cmd.exe", "powershell", "exploit"]
captura = pyshark.LiveCapture(interface=interfaz_red, display_filter=filtro_display)
datos_maliciosos = []
print("Buscando tráfico malicioso basado en firmas...\n")
for paquete in captura.sniff_continuously(packet_count=50):
    try:
        texto = ""
        if 'http' in paquete:
            if hasattr(paquete.http, 'user_agent'):
                texto += paquete.http.user_agent.lower()
            if hasattr(paquete.http, 'request_uri'):
                texto += paquete.http.request_uri.lower()
            if hasattr(paquete.http, 'host'):
                texto += paquete.http.host.lower()
        elif hasattr(paquete, 'tcp') and hasattr(paquete.tcp, 'payload'):
            texto += paquete.tcp.payload.lower()
        for firma in firmas_malware:
            if firma.lower() in texto:
                ip_origen = paquete.ip.src
                ip_destino = paquete.ip.dst
                hora = paquete.sniff_time.strftime("%H:%M:%S")
                print(f"[{hora}] ¡Tráfico malicioso detectado! {ip_origen} → {ip_destino} | Firma: {firma}")
                datos_maliciosos.append([hora, ip_origen, ip_destino, firma])
                break
    except AttributeError:
        continue
with open('detecciones_maliciosas.csv', mode='w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(['Hora', 'IP Origen', 'IP Destino', 'Firma Detectada'])
    escritor_csv.writerows(datos_maliciosos)
print("\nArchivo 'detecciones_maliciosas.csv' guardado con las detecciones.")
