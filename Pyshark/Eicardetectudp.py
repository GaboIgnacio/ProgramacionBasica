import pyshark
import csv
capture = pyshark.LiveCapture(interface='Wi-Fi')  # Cambia a tu interfaz real
paquetes_web = []
for packet in capture.sniff_continuously(packet_count=100):
    try:
        if hasattr(packet, 'dns'):
            source_address = packet.ip.src
            # Si es una consulta DNS
            if hasattr(packet.dns, 'qry_name'):
                dns_location = packet.dns.qry_name
                print(f"DNS Request from IP: {source_address} to DNS Name: {dns_location}")
                print(f"[DEBUG] dns_location capturado: {dns_location}")

                if "eicar.org" in dns_location:
                    print(" Dominio bloqueado: eso no!!!")
                    paquetes_web.append([dns_location])
                    break
            # Si es una respuesta DNS
            elif hasattr(packet.dns, 'resp_name'):
                dns_location = packet.dns.resp_name
                print(f"DNS Response from IP: {source_address} to DNS Name: {dns_location}")
                print(f"[DEBUG] dns_location capturado: {dns_location}")

                if "eicar.org" in dns_location:
                    print("Dominio bloqueado: eso no!!!")
                    paquetes_web.append([dns_location])
                    break
    except AttributeError:
        continue
if paquetes_web:
    with open("tráfico_web_dns2.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["DOMINIOS BLOQUEADOS"])
        writer.writerows(paquetes_web)

    print("\n Datos guardados en 'tráfico_web_dns2.csv'.")
else:
    print("\n No se detectó ningún dominio bloqueado. CSV no se generó.")
    