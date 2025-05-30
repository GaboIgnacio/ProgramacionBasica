# Identificar tráfico HTTP y extraer encabezados relevantes con guardado CSV al final
import pyshark
import csv
interfaz_red = 'Wi-Fi'  
filtro_display = 'http' 
captura = pyshark.LiveCapture(interface=interfaz_red, display_filter=filtro_display)
print("Capturando tráfico HTTP y extrayendo encabezados...\n")
datos_http = []
for paquete in captura.sniff_continuously(packet_count=10):
    try:
        metodo = paquete.http.request_method
        host = paquete.http.host
        uri = paquete.http.request_uri
        try:
            user_agent = paquete.http.user_agent
        except AttributeError:
            user_agent = 'N/A'
        try:
            referer = paquete.http.referer
        except AttributeError:
            referer = 'N/A'
        try:
            content_type = paquete.http.content_type
        except AttributeError:
            content_type = 'N/A'
        try:
            cookie = paquete.http.cookie
        except AttributeError:
                cookie = 'N/A'

        print(f"Método: {metodo} | Host: {host} | URI: {uri}")
        print(f"User-Agent: {user_agent}")
        print(f"Referer: {referer}")
        print(f"Content-Type: {content_type}")
        print(f"Cookie: {cookie}")
        print("-" * 50)

        datos_http.append([metodo, host, uri, user_agent, referer, content_type, cookie])

    except AttributeError:
        continue

# Guardar todos los datos al final en CSV
with open('encabezados_http.csv', mode='w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(['Método', 'Host', 'URI', 'User-Agent', 'Referer', 'Content-Type', 'Cookie'])
    escritor_csv.writerows(datos_http)

print("\nCaptura finalizada. Datos guardados en 'encabezados_http.csv'")
