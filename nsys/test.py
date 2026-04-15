import serial

# Configure the serial port
# For Windows: port='COM3'
# For Linux: port='/dev/ttyUSB0'
ser = serial.Serial(
    port='/dev/rfcomm0', 
    baudrate=115200, 
    timeout=1  # Important: prevents blocking forever if no data arrives
)

try:
    while True:
        if ser.in_waiting > 0:  # Check if data is available in the buffer
            # Read a line of data
            line = ser.readline().decode('utf-8').rstrip()
            print(f"Received: {line}")
except KeyboardInterrupt:
    print("Closing connection...")
finally:
    ser.close()  # Always close the port when finished
