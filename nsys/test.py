import serial
import time

# Configure the serial port
# For Windows, use names like 'COM3'. For Linux/Mac, use '/dev/ttyUSB0' or similar.
ser = serial.Serial(port='/dev/rfcomm0', baudrate=115200, timeout=1)

try:
    while True:
        # Read data until a newline character (\n) is received
        if ser.in_waiting > 0:
            line = ser.readall()
            print(f"Received: {line}")
            time.sleep(20)

except KeyboardInterrupt:
    print("Closing port...")
finally:
    ser.close()
