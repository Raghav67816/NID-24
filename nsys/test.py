import serial

# Open the serial port
# The baud rate often doesn't matter for RFCOMM as it's handled by the BT stack, 
# but the remote device might expect a specific rate in its configuration.
ser = serial.Serial('/dev/rfcomm0', 9600) 

while True:
    # Read a line of data or a specific number of bytes
    result = ser.readline() 
    print(result)
