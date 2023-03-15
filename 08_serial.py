import serial
import serial.tools.list_ports

# How to obtain all ports available
ports = serial.tools.list_ports.comports(include_links=False)
print([x.device for x in ports])

# Quick Script to connect to the only or first port available
if len(ports) == 1:
    SERIAL = ports[0].device
    print("Info: Using port COM: " + SERIAL)
else:
    if len(ports) == 0:
        print("Error: No port COM found")
    else:
        SERIAL = ports[0].device
        print("Warning: More that one port COM found, using first available: " + SERIAL)

# create an object _serial connecting to port SERIAL, baud rate 57600
_serial = serial.Serial(SERIAL, 57600)

# Write to serial port
_serial.write(b'Z400\n')
# read line from serial port
A = _serial.readline()
print(A.decode("utf-8"))

#flush the data from serial port
_serial.flush()

#end communication with the serial port
_serial.close()
