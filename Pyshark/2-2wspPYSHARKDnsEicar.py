import pyshark
capture = pyshark.LiveCapture(interface='Wi-Fi')
for packet in capture:
    try:
        if hasattr(packet, 'udp') and packet[packet.transport_layer].dstport == '53':
            if packet.dns.qry_name:
                source_address = packet.ip.src
                dns_location = packet.dns.qry_name
                print(f'DNS Request from IP: {source_address} to DNS Name: {dns_location}')
            elif packet.dns.resp_name:
                source_address = packet.ip.src
                dns_location = packet.dns.resp_name
                print(f'DNS Response from IP: {source_address} to DNS Name: {dns_location}')
            if dns_location == "eicar.org":
                print("eicar detectado")
                break
    except AttributeError as error:
        pass
    