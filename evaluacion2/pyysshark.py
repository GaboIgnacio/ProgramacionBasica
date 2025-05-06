import pyshark
interfaces = pyshark.LiveCapture().interfaces
print(interfaces)