import pyshark
import csv
capture = pyshark.LiveCapture(interface='Wi-Fi', display_filter='dns')
dominios = {}
max_paquetes = 100
contador = 0
for packet in capture:
    try:
        dominio = packet.dns.qry_name
        if dominio in dominios: # Si el dominio ya está en el diccionario dominios aumentamos su contador en 1.
            dominios[dominio] += 1
        else:
            dominios[dominio] = 1
        contador += 1
    except:
        continue
    if contador >= max_paquetes:
        break
lista_dominios = list(dominios.keys())
consultas = list(dominios.values())
# Compara cada consulta con las siguientes y las ordena en orden de mayor a menor 
# Cuando se encuentra una consulta mayor en consultas[j] que en consultas[i],
# se intercambian ambas consultas y también los dominios correspondientes para mantener el orden.
for i in range(len(consultas)):
    for j in range(i + 1, len(consultas)):
        if consultas[j] > consultas[i]:
            consultas[i], consultas[j] = consultas[j], consultas[i]
            lista_dominios[i], lista_dominios[j] = lista_dominios[j], lista_dominios[i]
print("\n Dominios consultados:")
for i in range(min(5, len(lista_dominios))):
    print(f"{lista_dominios[i]} → {consultas[i]} consultas")

with open('top5_dominios.csv', 'w', newline="") as file:
    writer = csv.writer(file)
    writer.writerow(['Dominio', 'Consultas'])
    for i in range(min(5, len(lista_dominios))):
        writer.writerow([lista_dominios[i], consultas[i]])

