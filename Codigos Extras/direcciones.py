# Este código sirve para solicitar al usuario información de varios paquetes de red (IP de origen y destino, y sus puertos), 
# almacenarla en listas y mostrarla organizada en forma de tabla.
ip_origen = []
ip_destino = []
puerto_origen = []
puerto_destino = []

cantidad = int(input("ingresa cantidad: "))
for i in range(cantidad):
    print(f"\n paquete {i+1}:")
    ip_origen.append(input("ingrese la IP de Origen: "))
    ip_destino.append(input("ingrese la IP de Destino: "))
    puerto_origen.append(int(input("ingrese el Puerto de Origen: ")))
    puerto_destino.append(int(input("ingrese el Puerto de Destino: ")))
print("="*70)
print(f"{'IP Origen':<15}{'IP Destino':<15}{'Puerto Origen':<15}{'Puerto Destino'}")
print("-"*70)
for ip_o, ip_d, p_o, p_d in zip(ip_origen, ip_destino, puerto_origen, puerto_destino):
    print(f"{ip_o:<10}{ip_d:<10}{p_o:<10}{p_d}")
    print("="*70)