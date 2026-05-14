import sys
import serial
from time import sleep
from numpy import load
from struct import pack

"""
write data to serial port at specified baud rate and frequency

params: 
path_to_file
port
baud rate by default -> 115200 
frequency by default -> 1KHz
"""

def write_to_serial(
    path: str,
    port: str,
    baud_rate: int = 115200,
    frequency: float = 1000    
):
    index = 0
    data = load(path)

    ch1 = data[0]
    ch2 = data[1]
    ch3 = data[2]

    try:
        with serial.Serial(port, timeout=1, baudrate=baud_rate) as serial_port:
            while True:
                ar = bytearray(pack(
                    '<3f',
                    float(ch1[index]),
                    float(ch2[index]),
                    float(ch3[index])
                ))

                serial_port.write(ar)
                index += 1

                sleep(1/frequency)

    except KeyboardInterrupt:
        return 0
    

write_to_serial(
    sys.argv[1],
    sys.argv[2]
)
