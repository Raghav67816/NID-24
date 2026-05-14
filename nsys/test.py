import serial

# Configure the serial port
# For Windows: Use 'COM3', 'COM4', etc.
# For Linux: Use '/dev/ttyUSB0' or '/dev/ttyACM0'
ser = serial.Serial(
    port='/dev/rfcomm0',      # Replace with your actual port
    baudrate=115200,    # Must match the device's baud rate
)

try:
    while True:
        # Check if data is available
        line = ser.readall()       # Read until a '\n' is received
        print(line) # Decode bytes and remove extra whitespace
except KeyboardInterrupt:
    print("Stopping...")
finally:
    ser.close() # Always close the port when done
