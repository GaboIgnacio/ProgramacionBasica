# egistrar información de varios paquetes de red ingresados por el usuario, 
# incluyendo IP de origen y destino, puertos, y el protocolo usado (TCP o UDP), 
# y luego mostrar todos los datos organizados en una tabla. 
ip_origen = []
ip_destino = []
puerto_origen = []
puerto_destino = []
protocolo = []

cantidad = int(input("Ingresa cantidad de paquetes: "))
for i in range(cantidad):
    print(f"\nPaquete {i+1}:")
    ip_origen.append(input("Ingrese la IP de Origen: "))
    ip_destino.append(input("Ingrese la IP de Destino: "))
    puerto_origen.append(int(input("Ingrese el Puerto de Origen: ")))
    puerto_destino.append(int(input("Ingrese el Puerto de Destino: ")))
    protocolo.append(input("Ingrese el protocolo (TCP o UDP): "))

print("="*100)
print(f"{'IP Origen':<15}{'IP Destino':<15}{'Puerto Origen':<15}{'Puerto Destino':<17}{'Protocolo'}")
print("-"*100)
for ip_o, ip_d, p_o, p_d, proto in zip(ip_origen, ip_destino, puerto_origen, puerto_destino, protocolo):
    print(f"{ip_o:<15}{ip_d:<15}{p_o:<15}{p_d:<17}{proto}")
    print("="*100)
 