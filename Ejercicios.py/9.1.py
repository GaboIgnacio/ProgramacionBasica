# Detectar paquetes con direcciones IP privadas según RFC 1918.
import pyshark
import csv
interfaz = 'Wi-Fi'
filtro = 'ip'
captura = pyshark.LiveCapture(interface=interfaz, display_filter=filtro)
paquetes_privados = []
print("Detectando paquetes con direcciones IP privadas...\n")
def es_ip_privada(ip):
    if ip.startswith("10."): # Revisa si la IP empieza con "10."
        return True
    if ip.startswith("192.168."): # Revisa si la IP empieza con "192.168." 
        return True
    if ip.startswith("172."): # Para la red privada clase B, verifica si empieza con "172."
        segundo = int(ip.split(".")[1]) # Separa la IP por puntos y convierte el segundo octeto a entero
        if 16 <= segundo <= 31:  # Verifica si el segundo octeto está entre 16 y 31
            return True
    return False
for paquete in captura.sniff_continuously(packet_count=10):
    try:
        ip_origen = paquete.ip.src # Extrae la IP de origen del paquete
        ip_destino = paquete.ip.dst # Extrae la IP de destino del paquete
        hora = paquete.sniff_time.strftime("%H:%M:%S") # Extrae la hora en que se capturó el paquete, formato HH:MM:SS
        # Determina si la IP de origen es privada o pública usando la función anterior
        tipo_origen = "Privada" if es_ip_privada(ip_origen) else "Pública"
        # Determina si la IP de destino es privada o pública usando la función anterior
        tipo_destino = "Privada" if es_ip_privada(ip_destino) else "Pública"
        # Solo si alguna de las IPs (origen o destino) es privada, imprime y guarda
        if tipo_origen == "Privada" or tipo_destino == "Privada":
            print(f"[{hora}] {ip_origen} ({tipo_origen}) → {ip_destino} ({tipo_destino})")
            paquetes_privados.append([hora, ip_origen, ip_destino, f"{tipo_origen} → {tipo_destino}"])
    except AttributeError:
        continue                                  # (codificación UTF-8 para evitar errores)
with open('ip_privadas.csv', mode='w', newline='', encoding='utf-8') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['Hora', 'IP Origen', 'IP Destino', 'Tipo'])
    escritor.writerows(paquetes_privados)
print("\n Archivo 'ip_privadas.csv' guardado con direcciones IP privadas detectadas.")
