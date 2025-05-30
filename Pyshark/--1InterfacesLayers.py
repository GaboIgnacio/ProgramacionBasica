import pyshark

cap = pyshark.LiveCapture()
print(cap.interfaces)


#capture = pyshark.LiveCapture(interface='Wi-fi')
# for packet in capture:
# layers = packet.layers
# print(layers)
