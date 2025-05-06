# Este código sirve para obtener e imprimir una lista de las interfaces de red 
# disponibles en el sistema utilizando la biblioteca `pyshark`. 
# `pyshark.LiveCapture().interfaces` devuelve información
#  sobre las interfaces de red detectadas en la máquina donde se ejecuta el código.
import pyshark
interfaces = pyshark.LiveCapture().interfaces
print(interfaces)
