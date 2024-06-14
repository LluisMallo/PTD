import serial

BAUD_RATE = 9600
# nom_port = '/dev/cu.usbserial-1420' #APC
nom_port = "/dev/ttyUSB0"  # Arduino cable

cansat = serial.Serial(nom_port, BAUD_RATE)

while True:
    missatge = input(f"Quin missatge vols enviar?: ")

    missatge_bytes = missatge.encode('Ascii')
    cansat.write(missatge_bytes)
                    


print("Adeu!")
cansat.close() # Tanca el port
