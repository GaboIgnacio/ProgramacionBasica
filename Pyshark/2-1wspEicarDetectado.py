import pyshark
capture = pyshark.LiveCapture(interface='Wi-Fi', display_filter='dns')
for packet in capture:
    try:
        if hasattr(packet, 'dns') and hasattr(packet.dns, 'qry_name'):
            query_name = packet.dns.qry_name.lower()
            print(f"Consulta DNS detectada: {query_name}")
            if 'eicar' in query_name:
                print(" Tráfico hacia eicar detectado")
                break
    except AttributeError:
        pass
    