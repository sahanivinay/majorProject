import serial
import csv

# Define the serial port and baud rate
serial_port = '/dev/ttyUSB0'  # Modify this based on your BeagleBone's configuration
baud_rate = 9600

# Define the CSV file name
csv_filename = 'love_hope.csv'

# Define the number of samples to collect
num_samples = 10

try:
    # Open the serial port
    with serial.Serial(serial_port, baud_rate) as ser:
        # Open the CSV file in write mode
        with open(csv_filename, mode='w', newline='') as csv_file:
            # Create a CSV writer object
            csv_writer = csv.writer(csv_file)
            
            # Write the header row
            csv_writer.writerow(['f1', 'f2', 'f3', 'f4', 'f5', 'mpu1', 'mpu2', 'mpu3'])
            
            sample_count = 0
            # Read data from the serial port until 100 samples are collected
            while sample_count < num_samples:
                # Read a line of data from the serial port
                line = ser.readline().decode('utf-8').strip()
                
                # Print the received line for debugging
                print("Received:", line)
                
                # Split the received data into flex sensor and MPU values
                data_parts = line.split(', ')
                flex_values = [int(value) for value in data_parts[:5]]
                mpu_values = [int(value) for value in data_parts[5:]]
                
                # Write the data to the CSV file
                csv_writer.writerow(flex_values + mpu_values)
                
                sample_count += 1
                
except serial.SerialException as e:
    print("Error:", e)
