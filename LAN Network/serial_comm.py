import serial
import csv

ser = serial.Serial('/dev/ttyAMA0', 115200)

while True:
    
    recieved_data = ser.readline().decode('utf-8').rstrip()
    print(f"Recied Data: {recieved_data}")

    with open('belt_speed.txt', 'w') as file:
        combined = ''.join(recieved_data)
        file.write(combined)

