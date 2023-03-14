import serial
import serial.tools.list_ports

ports = serial.tools.list_ports.comports(include_links=False)
print([x.device for x in ports])

if len(ports) == 1:
    SERIAL = ports[0].device
    print("Info: Using port COM: " + SERIAL)
else:
    if len(ports) == 0:
        print("Error: No port COM found")
    else:
        SERIAL = ports[0].device
        print("Warning: More that one port COM found, using first available: " + SERIAL)


_serial = serial.Serial(SERIAL, 57600)
_serial.write(b'Z400\n')
A = _serial.readline()
print(A.decode("utf-8"))

_serial.flush()
_serial.close()
