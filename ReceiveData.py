import serial

# Define the COM port
COM_PORT = 'COM3'
# Define the baudrate
BAUD_RATE = 9600

# Create a serial object
ser = serial.Serial(COM_PORT, BAUD_RATE)

try:
    while True:
        # Read a line of data from the serial port
        data = ser.readline().decode().strip()
        
        # Print the received data
        print("Received:", data)
        
        # You can add further processing of the received data here
        
except KeyboardInterrupt:
    # Close the serial port when the program is terminated
    ser.close()
